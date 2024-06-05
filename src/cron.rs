use tokio::time::{self, Duration};
use reqwest::Client;
use serde::Serialize;
use std::env;
use dotenv::dotenv;

#[derive(Serialize)]
struct PostData {
    key: String,
    value: String,
}

async fn make_requests(client: &Client) -> Result<(), Box<dyn std::error::Error>> {
    // Fetch the API endpoints dynamically from environment variables
    let get_url = env::var("GET_URL")?;
    let post_url = env::var("POST_URL")?;

    // Make a GET request
    let get_response = client.get(&get_url).send().await?;
    println!("GET Response: {:?}", get_response.text().await?);

    // Define the POST data
    let post_data = PostData {
        key: "example_key".to_string(),
        value: "example_value".to_string(),
    };

    // Make a POST request
    let post_response = client.post(&post_url)
        .json(&post_data)
        .send().await?;
    println!("POST Response: {:?}", post_response.text().await?);

    Ok(())
}

#[tokio::main]
async fn main() {
    // Load environment variables from a .env file
    dotenv().ok();

    // Create an HTTP client
    let client = Client::new();

    // Set up the interval for the cron job
    let mut interval = time::interval(Duration::from_secs(300));

    loop {
        interval.tick().await;
        match make_requests(&client).await {
            Ok(_) => println!("Requests completed successfully"),
            Err(e) => eprintln!("Error making requests: {}", e),
        }
    }
}
