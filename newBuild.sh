echo"Starting a new build..."
echo"Building..."
sudo docker build -t breadbot .
echo"Build complete!"
echo"Starting container..."
sudo docker run -d -p breadbot:latest
echo"Container started!"
echo"Done!"