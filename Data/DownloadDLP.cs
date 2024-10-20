using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq; // Make sure to install Newtonsoft.Json via NuGet
using System.Runtime.InteropServices;
using QuickTools.QCore; 
class DownloadDLP
{
private static readonly HttpClient client = new HttpClient
{
    Timeout = TimeSpan.FromMilliseconds(60000*10) // Set a longer timeout
};
public static bool IsLinux()
{
    return RuntimeInformation.IsOSPlatform(OSPlatform.Linux);
}

public static bool IsWindows()
{
    return RuntimeInformation.IsOSPlatform(OSPlatform.Windows);
}
public static async Task Download(string link_to_dlp)
{
    if(!string.IsNullOrEmpty(link_to_dlp))
        dlp_link = link_to_dlp;
    await Download();
}
private static string dlp_link = "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest";
public static async Task Download()
{
    var latestReleaseUrl = dlp_link;
    var downloadUrl = await GetLatestReleaseDownloadUrl(latestReleaseUrl);
    
    if (downloadUrl != null)
    {
        Get.Box("Downloading from: " + downloadUrl);
        if(IsWindows())
        {
            await DownloadFile(downloadUrl, "yt-dlp.exe");
        }if(IsLinux())
        {
            await DownloadFile(downloadUrl, "yt-dlp_linux");
        }
    }
    else
    {
        Console.WriteLine("Could not find the download URL.");
    }
}

private static async Task<string> GetLatestReleaseDownloadUrl(string url)
{
    client.DefaultRequestHeaders.Add("User-Agent", "YourApplicationName"); // Set User-Agent here
    var response = await client.GetStringAsync(url);
    var json = JObject.Parse(response);
    var assets = json["assets"];

    foreach (var asset in assets)
    {
        var name = asset["name"].ToString();
        Get.Blue($"Available..: {name}");
        if(IsWindows())
        {
             if (name.EndsWith(".exe")) // Check for executable files
            {
                return asset["browser_download_url"].ToString();
            }
        }if(IsLinux())
        {
            if (name.EndsWith("_linux")) // Check for executable files
            {
                return asset["browser_download_url"].ToString();
            }
        }
       
    }
    return null;
}

private static async Task DownloadFile(string url, string outputPath)
{
    var response = await client.GetAsync(url);
    response.EnsureSuccessStatusCode();

    using (var fs = new System.IO.FileStream(outputPath, System.IO.FileMode.Create, System.IO.FileAccess.Write, System.IO.FileShare.None))
    {
        await response.Content.CopyToAsync(fs);
    }
}

}
