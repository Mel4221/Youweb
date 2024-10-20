# ==============================
# Stage 1: Build
# ==============================
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python packages one by one
RUN pip3 install eyed3 --break-system-packages
RUN pip3 install pathlib --break-system-packages
RUN pip3 install pytube --break-system-packages
RUN pip3 install pytubefix --break-system-packages
RUN pip3 install moviepy --break-system-packages
RUN pip3 install regex --break-system-packages
RUN pip3 install emoji --break-system-packages
RUN pip3 install ffmpeg --break-system-packages
RUN pip3 install pathvalidate --break-system-packages

# ==============================
# Set the working directory
# ==============================
WORKDIR /app

# Copy the project file and restore dependencies
COPY Youweb.csproj ./
RUN dotnet restore

# Copy the rest of the application
COPY . ./

# Build the application
RUN dotnet publish -c Release -o out

# ==============================
# Stage 2: Final build
# ==============================
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Python packages one by one
RUN pip3 install eyed3 --break-system-packages
RUN pip3 install pathlib --break-system-packages
RUN pip3 install pytube --break-system-packages
RUN pip3 install pytubefix --break-system-packages
RUN pip3 install moviepy --break-system-packages
RUN pip3 install regex --break-system-packages
RUN pip3 install emoji --break-system-packages
RUN pip3 install ffmpeg --break-system-packages
RUN pip3 install pathvalidate --break-system-packages

# Set the working directory
WORKDIR /app

# Copy the build output from the previous stage
COPY --from=build /app/out .

# Expose port 8080
EXPOSE 8080

# Specify the entry point for the application
ENTRYPOINT ["dotnet", "Youweb.dll"]
