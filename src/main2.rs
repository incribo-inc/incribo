use std::fs::{File, metadata};
use std::io::{BufReader, BufWriter};
use zstd::stream::{copy_encode, copy_decode};
use std::error::Error;
use csv::Reader;
use serde::Deserialize;
use rust_bert::pipelines::sentence_embeddings::{SentenceEmbeddingsBuilder, SentenceEmbeddingsModelType};
use tch::Device;

#[derive(Debug, Deserialize)]
struct Record {
    text: String,
}


// Function to compress a CSV file
fn compress_csv(input_path: &str, output_path: &str) -> Result<(), Box<dyn Error>> {
    let input_file = File::open(input_path)?;
    let output_file = File::create(output_path)?;

    let mut reader = BufReader::new(input_file);
    let mut writer = BufWriter::new(output_file);

    copy_encode(&mut reader, &mut writer, 0)?;

    Ok(())
}

// Function to decompress a CSV file
fn decompress_csv(input_path: &str, output_path: &str) -> Result<(), Box<dyn Error>> {
    let input_file = File::open(input_path)?;
    let output_file = File::create(output_path)?;

    let mut reader = BufReader::new(input_file);
    let mut writer = BufWriter::new(output_file);

    copy_decode(&mut reader, &mut writer)?;

    Ok(())
}

// Function to read CSV data and collect text
fn read_csv(file_path: &str) -> Result<Vec<String>, Box<dyn Error>> {
    let mut rdr = Reader::from_path(file_path)?;
    let mut texts = Vec::new();
    for result in rdr.deserialize() {
        let record: Record = result?;
        texts.push(record.text);
    }
    Ok(texts)
}

// Function to get file size in bytes
fn get_file_size(path: &str) -> Result<u64, Box<dyn Error>> {
    let metadata = metadata(path)?;
    Ok(metadata.len())
}

// Function to convert bytes to a readable format (MB, GB)
fn format_size(bytes: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = KB * 1024;
    const GB: u64 = MB * 1024;

    if bytes >= GB {
        format!("{:.2} GB", bytes as f64 / GB as f64)
    } else if bytes >= MB {
        format!("{:.2} MB", bytes as f64 / MB as f64)
    } else if bytes >= KB {
        format!("{:.2} KB", bytes as f64 / KB as f64)
    } else {
        format!("{} bytes", bytes)
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let input_path = "test-data.csv";
    let compressed_path = "data.csv.zst";
    let decompressed_path = "data_decompressed.csv";

    // Compress the CSV file
    compress_csv(input_path, compressed_path)?;

    // Decompress the CSV file
    decompress_csv(compressed_path, decompressed_path)?;

    // Read the CSV data
    let texts = read_csv(decompressed_path)?;

    // Load the embedding model
    let device = Device::cuda_if_available();
    let embeddings_model = SentenceEmbeddingsBuilder::remote(SentenceEmbeddingsModelType::AllMiniLmL12V2)
        .with_device(device)
        .create_model()?;

    // Get embeddings
    let embeddings = embeddings_model.encode(&texts)?;

    // Print the embeddings
    println!("Embeddings: {:?}", embeddings);

    // Get and print the sizes of the files
    let input_size = get_file_size(input_path)?;
    let compressed_size = get_file_size(compressed_path)?;
    let decompressed_size = get_file_size(decompressed_path)?;

    println!("Size of original CSV ({}): {}", input_path, format_size(input_size));
    println!("Size of compressed CSV ({}): {}", compressed_path, format_size(compressed_size));
    println!("Size of decompressed CSV ({}): {}", decompressed_path, format_size(decompressed_size));

    Ok(())
}

