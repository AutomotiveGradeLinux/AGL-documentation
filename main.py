"""mkdocs-macros-plugin hook module.

Computes derived release-identity values from the `extra:` variables in
mkdocs.yml, so pages can reference them as plain Jinja variables (e.g.
`{{ agl_download_base }}`) instead of hardcoding branch names or URL
shapes that change every AGL release.
"""


def define_env(env):
    agl = env.variables["agl"]
    kind = env.variables["artifact_kind"]
    # Pre-cut/rolling builds always live under the "master" ref regardless
    # of the upcoming release's codename; only "release" mode uses the
    # AGL codename as the path segment.
    ref = agl["codename"] if kind == "release" else "master"
    env.variables["agl_download_base"] = (
        f"https://download.automotivelinux.org/AGL/{kind}/{ref}"
    )
