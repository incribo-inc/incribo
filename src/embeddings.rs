use std::fs::File;
use std::io::{BufReader, BufWriter};
use std::path::Path;
use zstd::stream::{copy_encode, copy_decode};

// Function to compress a CSV file
fn compress_csv(input_path: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let input_file = File::open(input_path)?;
    let output_file = File::create(output_path)?;

    let mut reader = BufReader::new(input_file);
    let mut writer = BufWriter::new(output_file);

    copy_encode(&mut reader, &mut writer, 0)?;

    Ok(())
}

// Function to decompress a CSV file
fn decompress_csv(input_path: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let input_file = File::open(input_path)?;
    let output_file = File::create(output_path)?;

    let mut reader = BufReader::new(input_file);
    let mut writer = BufWriter::new(output_file);

    copy_decode(&mut reader, &mut writer)?;

    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let input_path = "test-data.csv";
    let compressed_path = "data.csv.zst";
    let decompressed_path = "data_decompressed.csv";

    // Compress the CSV file
    compress_csv(input_path, compressed_path)?;

    // Decompress the CSV file
    decompress_csv(compressed_path, decompressed_path)?;

    Ok(())
}