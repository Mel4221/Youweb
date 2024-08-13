using System.Text.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System;
using System.IO;
 namespace Youweb.Data
{
         public partial class UShare
        {
                private string _filePath{get;set;}
                                // Method to read the JSON file and return it as a JObject
                public JObject ReadJson()
                {
                        if (!File.Exists(_filePath))
                        {
                                throw new FileNotFoundException("The JSON file does not exist.");
                        }

                        var json = File.ReadAllText(_filePath);
                        return JObject.Parse(json);
                }

                // Method to write a JObject to the JSON file
                public void WriteJson(JObject jsonObject)
                {
                        var json = jsonObject.ToString(Formatting.Indented);
                        File.WriteAllText(_filePath, json);
                }
        }
}