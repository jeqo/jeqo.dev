const std = @import("std");
const zine = @import("zine");

pub fn build(b: *std.Build) !void {
    zine.website(b, .{
        .title = "jeqo-website",
        .host_url = "https://jeqo.dev",
        .content_dir_path = "content",
        .layouts_dir_path = "layouts",
        .assets_dir_path = "assets",
        .static_assets = &.{
            "CNAME",
            "favicon.ico",
            "styles/main.css",
            "styles/fonts.css",
            "styles/highlight.css",
            "fonts/Spectral-Regular.woff2",
            "fonts/Spectral-Medium.woff2",
            "fonts/Spectral-Light.woff2",
            "fonts/Spectral-ExtraLight.woff2",
            "fonts/Spectral-Italic.woff2",
            "fonts/Spectral-SemiBold.woff2",
            "fonts/JetBrainsMono-Regular.woff2",
            "fonts/JetBrainsMono-Italic.woff2",
            "fonts/JetBrainsMono-Medium.woff2",
            "fonts/JetBrainsMono-Light.woff2",
            "fonts/JetBrainsMono-Bold.woff2",
        },
    });
}
