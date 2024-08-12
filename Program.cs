using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using Youweb.Data;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.FileProviders;
using System.IO;
using Microsoft.AspNetCore.Http.Features;


var builder = WebApplication.CreateBuilder(args);
/*
builder.Services.AddDistributedMemoryCache(); // Adds a default in-memory implementation of IDistributedCache
builder.Services.AddSession(options =>
{
    options.IdleTimeout = TimeSpan.FromMinutes(20); // Set session timeout
    options.Cookie.HttpOnly = true;
    options.Cookie.IsEssential = true;
});
*/

/*
// Configure Kestrel to increase the maximum request body size
builder.WebHost.ConfigureKestrel(options =>
{
    options.Limits.MaxRequestBodySize = 104857600; // 100 MB
});

// Configure IIS server options if using IIS
builder.Services.Configure<IISServerOptions>(options =>
{
    options.MaxRequestBodySize = 104857600; // 100 MB
});
*/

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
//builder.Services.AddSingleton<WeatherForecastService>();
// Add distributed memory cache
builder.Services.AddDistributedMemoryCache();

// Configure session state with a very short timeout
/*
builder.Services.AddSession(options =>
{
    options.IdleTimeout = TimeSpan.FromSeconds(60); // Set the timeout to 1 second
    options.Cookie.HttpOnly = true;
    options.Cookie.IsEssential = true;
    
});
*/
var app = builder.Build();

/*
    Added feature but needs to be disabled 
    if needed
*/
/*
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new PhysicalFileProvider(Path.Combine(Directory.GetCurrentDirectory(), "/home")),
    RequestPath = "/home"
});
*/

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}





app.UseHttpsRedirection();


app.UseRouting();
app.UseStaticFiles();
app.UseAuthorization();
//app.UseSession(); // Enable session middleware
 

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
