use csv::Reader;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct EmbeddingRecord {
    // Define the CSV schema 
    id: String,
    embedding: Vec<f64>
}

fn read_csv(file_path: &str) -> Result<Vec<EmbeddingRecord>, Box<dyn std::error::Error>> {
    let mut rdr = Reader::from_path(file_path)?;
    let mut records = Vec::new();
    
    for result in rdr.deserialize() {
        let record: EmbeddingRecord = result?;
        records.push(record);
    }
    
    Ok(records)
}
