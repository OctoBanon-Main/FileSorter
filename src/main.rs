use std::fs::create_dir_all;

fn create_directories() {
    let directories = vec![
        "Audio",
        "Videos",
        "Photos",
        "Icons",
        "Archives",
        "Other",
        "Executable",
        "Disk Images",
        "3D Models"
    ];

    for directory in &directories {
        if let Err(err) = create_dir_all(directory) {
            eprintln!("Failed to create directory {}: {}", directory, err);
        } else {
            println!("Created directory: {}", directory);
        }
    }
}

fn main() {
    create_directories();
}
