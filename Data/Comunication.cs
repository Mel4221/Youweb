using System.Text.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System;
using System.IO;
namespace Youweb.Data
{

        public class UMessage
        {
                public string Action{get;set;}
                public string Type{get;set;} 
                public string Arguments{get;set;} 
                public string? Summary { get; set; }

        }
        public partial class UShare
        {
         //       private readonly string _filePath;
                    // Method to update a specific node in the JSON file
    public void UpdateNode(string nodePath, JToken newValue)
    {
        var jsonObject = ReadJson();
        var node = jsonObject.SelectToken(nodePath);

        if (node == null)
        {
            throw new ArgumentException("Node path not found.");
        }

        node.Replace(newValue);
        WriteJson(jsonObject);
    }
                public void Send()
                {
                        /*
                        @Required Property:         public string? Summary { get; set; }
                        string fileName = "WeatherForecast.json";
                        await using FileStream createStream = File.Create(fileName);
                        await JsonSerializer.SerializeAsync(createStream, weatherForecast);
                        */

                }
        }
}