using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Youweb.Data
{

public class JMetadata
{
    private readonly string _filePath;
    private JObject _jsonObject;

    public JMetadata(string filePath)
    {
        _filePath = filePath;
        LoadJson();
    }

    private void LoadJson()
    {
        if (File.Exists(_filePath))
        {
            string jsonString = File.ReadAllText(_filePath);
            _jsonObject = JObject.Parse(jsonString);
        }
        else
        {
            _jsonObject = new JObject(); // Create an empty JObject if file does not exist
        }
    }

    public JToken GetValue(string path)
    {
        return _jsonObject.SelectToken(path);
    }

    public void SetValue(string path, JToken value)
    {
        var token = _jsonObject.SelectToken(path);
        if (token != null)
        {
            token.Replace(value);
        }
        else
        {
            // Add new property to the JSON object
            var parentPath = GetParentPath(path);
            var propertyName = GetPropertyName(path);

            var parentToken = _jsonObject.SelectToken(parentPath) as JObject;
            if (parentToken != null)
            {
                parentToken[propertyName] = value;
            }
            else
            {
                // If the parent path does not exist, create it
                var newParent = new JObject { [propertyName] = value };
                var pathParts = parentPath.Split('.');
                var currentObject = _jsonObject;

                for (int i = 0; i < pathParts.Length; i++)
                {
                    if (i == pathParts.Length - 1)
                    {
                        currentObject[pathParts[i]] = newParent;
                    }
                    else
                    {
                        if (currentObject[pathParts[i]] == null)
                        {
                            currentObject[pathParts[i]] = new JObject();
                        }
                        currentObject = (JObject)currentObject[pathParts[i]];
                    }
                }
            }
        }
        SaveJson();
    }

    public void UpdateValue(string path, JToken newValue)
    {
        var token = _jsonObject.SelectToken(path);
        if (token != null)
        {
            token.Replace(newValue);
            SaveJson();
        }
        else
        {
            throw new Exception("Path not found in JSON.");
        }
    }

    private void SaveJson()
    {
        string jsonString = _jsonObject.ToString(Formatting.Indented);
        File.WriteAllText(_filePath, jsonString);
    }

    private string GetParentPath(string path)
    {
        var lastDotIndex = path.LastIndexOf('.');
        return lastDotIndex == -1 ? "" : path.Substring(0, lastDotIndex);
    }

    private string GetPropertyName(string path)
    {
        var lastDotIndex = path.LastIndexOf('.');
        return lastDotIndex == -1 ? path : path.Substring(lastDotIndex + 1);
    }
}

/*
class Program
{
    static void Main()
    {
        string filePath = "data.json";
        var manager = new JsonFileManager(filePath);

        // Set a value
        manager.SetValue("user.name", "mario");

        // Update a value
        manager.UpdateValue("user.name", "luigi");

        // Get a value
        var value = manager.GetValue("user.name");
        Console.WriteLine($"User name: {value}");
    }
}

*/
}