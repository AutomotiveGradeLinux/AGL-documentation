---
title: meta-agl-demo
---

## Introduction

The `meta-agl-demo` layer is the reference user interface layer for the DEMO
platform of Automotive Grade Linux (AGL).
The layer provides a reference platform and applications.
The BitBake target name for the DEMO platform is `agl-ivi-demo-qt`, which is
the full DEMO platform image.

## Layer Dependencies

This section describes dependencies for the `meta-agl-demo` layer.
Dependencies are grouped into base, hardware, and feature dependencies.

### Base Dependencies

The `meta-agl-demo` layer has the following base dependencies:

- Yocto Project Release:

    - URI: git://git.yoctoproject.org/poky
    - Branch: "kirkstone"
    - Tested Revision: See the
      [`default.xml`](https://github.com/leon-anavi/AGL-repo/blob/master/default.xml)
      manifest file for the `AGL-repo` repository for revision information.

- AGL `meta-agl` Layer:

    - URI: https://gerrit.automotivelinux.org/gerrit/AGL/meta-agl
    - Branch: "master"

- OpenEmbedded `meta-openembedded` Layer:

    Specifically, out of `meta-openembedded`, these sub-layers are used:

    - `meta-oe`
    - `meta-multimedia`
    - `meta-networking`
    - `meta-python`

- Yocto Project `meta-qt5` Layer from the
  [OpenEmbedded Layer Index](https://layers.openembedded.org/layerindex/branch/master/layers/):

    - URI: https://github.com/meta-qt5/meta-qt5.git

### Feature Dependencies

The `meta-agl-demo` layer has the following AGL [feature](../../01_Getting_Started/02_Building_AGL_Image/04_Initializing_Your_Build_Environment.md/#agl-features)
dependencies:

- Yocto Project `meta-security` Layer:

- OpenEmbedded's `meta-openembedded` Layer:

    - URI: https://github.com/openembedded/meta-openembedded
    - Branch: "kirkstone"
    - Tested Revision: See the
      [`default.xml`](https://github.com/leon-anavi/AGL-repo/blob/master/default.xml)
      manifest file for the `AGL-repo` repository for revision information.

    Specifically, out of `meta-openembedded`, these sub-layers are used:

    - `meta-filesystems`
    - `meta-oe`
    - `meta-python`

**The `agl-netboot` Feature:**

- AGL's `meta-netboot` Layer within the `meta-agl` Layer:

    - URI: https://gerrit.automotivelinux.org/gerrit/gitweb?p=AGL/meta-agl.git
    - Branch: "master"

## Maintenance

All patches must be submitted via the AGL Gerrit instance at
<https://gerrit.automotivelinux.org>.  See this wiki page for
details:

<https://wiki.automotivelinux.org/agl-distro/contributing>

Layer maintainers:

* Jan-Simon Möller <jsmoeller@linuxfoundation.org>


**Note:** For update details on this page please refer

<https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-demo.md>
