const std = @import("std");
const zine = @import("zine");

pub fn build(b: *std.Build) !void {
    zine.website(b, .{
        .title = "jeqo-website",
        .host_url = "https://jeqo.github.io",
        .content_dir_path = "content",
        .layouts_dir_path = "layouts",
        .assets_dir_path = "assets",
        .static_assets = &.{
            "styles/main.css",
            "fonts/Spectral-Regular.woff2",
            "fonts/Spectral-Italic.woff2",
            "fonts/Spectral-SemiBold.woff2",
            "fonts/JetBrainsMono-Regular.woff2",
            "fonts/JetBrainsMono-Bold.woff2",
        },
    });
}
