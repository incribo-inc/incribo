use mongodb::{Client, options::ClientOptions, bson::doc};
use mongodb::bson::Bson;
use serde_json::json;
use tokio;

async fn insert_into_mongodb(records: Vec<EmbeddingRecord>) -> mongodb::error::Result<()> {
    let client_options = ClientOptions::parse("mongodb://localhost:27017").await?;
    let client = Client::with_options(client_options)?;
    let database = client.database("cluster_0");
    let collection = database.collection("ai_embeddings");
    
    for record in records {
        let doc = doc! {
            "id": &record.id,
            "embedding": Bson::Array(record.embedding.iter().map(|v| Bson::Double(*v)).collect())
        };
        collection.insert_one(doc, None).await?;
    }
    
    Ok(())
}
