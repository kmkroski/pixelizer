# Pixelizer

Pixelizer is a small utility to create pixelized (retro video game style) images and videos.

Pixelizer applies the following steps in order:

1. Resizes the image (default is 256px wide).
2. Adjusts contrast and exposure
3. Replaces the images' colors with colors from a predefined palette.
4. Applies dithering to blend the colors.
5. While keeping each pixel square, scales up the image.

Palettes sourced from [Lospec's palette gallery](hhttps://lospec.com/palette-list).

## Install

Create a virtual environment and install the project locally so the `pixelizer`
CLI becomes available:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -e .
```

If you only need runtime deps, install from requirements:

```bash
pip install -r requirements.txt
```

## CLI Overview

After installation you can run `pixelizer` with one of three subcommands:

- `pixelizer image <input>` — pixelate a single image
- `pixelizer video <input>` — pixelate a video file
- `pixelizer sample <input>` — produce a grid of palettes and dither levels

## Options

All subcommands share these options:

- `-o, --output` Output path (default name is constructed from other options)
- `-w, --width` Pixelated image width in pixels (default: 256)
- `-s, --scale` Output scale factor applied to pixelated image (default: 4)
- `-p, --palette` Palette name to use (default: 'default')
- `-pf, --palette-file` YAML file containing palettes (name -> list of hex colors)
- `-d, --dither` Dither type (f|s|b1|b2|b3|b4|b5, default: b3)
- `-e, --exposure` Exposure multiplier (float, default: 1.0)
- `-c, --contrast` Contrast multiplier (float, default: 1.0)

## Usage

### Image

```bash
pixelizer image in.jpg -o out.png -w 160 -s 4 -p cboy -d s
```

### Video

```bash
pixelizer image in.webm -o out.mp4 -w 180 -s 2 -p dmg4 -d b2
```

### Sample

**Heads Up**: This takes quite a few minutes to run!

`--palette` and `--dither` are ignored.

```bash
pixelizer sample ex.jpg -w 128 -s 4
```

## Examples

The orginal image is located on [Wikimedia](https://upload.wikimedia.org/wikipedia/commons/d/dd/Buzz_salutes_the_U.S._Flag.jpg).

All images are scaled to have a final output width of 512px. Images with a width of 128px will have a scale of 4x.

The filenames can be decoded into the arguments: `astronaut_{PALETTE}_{DITHER}_{WIDTH}px_{SCALE}x.png`

### 512px
 
[Complete Sample Sheet](examples/astronaut_sample_512px_1x.png)
 
| Palette | Floyd | Sierra | Bayer 1 | Bayer 2 | Bayer 3 | Bayer 4 | Bayer 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *default* | ![default f 512px](examples/astronaut_default_f_512px_1x.png) | ![default s 512px](examples/astronaut_default_s_512px_1x.png) | ![default b1 512px](examples/astronaut_default_b1_512px_1x.png) | ![default b2 512px](examples/astronaut_default_b2_512px_1x.png) | ![default b3 512px](examples/astronaut_default_b3_512px_1x.png) | ![default b4 512px](examples/astronaut_default_b4_512px_1x.png) | ![default b5 512px](examples/astronaut_default_b5_512px_1x.png) |
| *nostalgia* | ![nostalgia f 512px](examples/astronaut_nostalgia_f_512px_1x.png) | ![nostalgia s 512px](examples/astronaut_nostalgia_s_512px_1x.png) | ![nostalgia b1 512px](examples/astronaut_nostalgia_b1_512px_1x.png) | ![nostalgia b2 512px](examples/astronaut_nostalgia_b2_512px_1x.png) | ![nostalgia b3 512px](examples/astronaut_nostalgia_b3_512px_1x.png) | ![nostalgia b4 512px](examples/astronaut_nostalgia_b4_512px_1x.png) | ![nostalgia b5 512px](examples/astronaut_nostalgia_b5_512px_1x.png) |
| *cc29* | ![cc29 f 512px](examples/astronaut_cc29_f_512px_1x.png) | ![cc29 s 512px](examples/astronaut_cc29_s_512px_1x.png) | ![cc29 b1 512px](examples/astronaut_cc29_b1_512px_1x.png) | ![cc29 b2 512px](examples/astronaut_cc29_b2_512px_1x.png) | ![cc29 b3 512px](examples/astronaut_cc29_b3_512px_1x.png) | ![cc29 b4 512px](examples/astronaut_cc29_b4_512px_1x.png) | ![cc29 b5 512px](examples/astronaut_cc29_b5_512px_1x.png) |
| *cboy* | ![cboy f 512px](examples/astronaut_cboy_f_512px_1x.png) | ![cboy s 512px](examples/astronaut_cboy_s_512px_1x.png) | ![cboy b1 512px](examples/astronaut_cboy_b1_512px_1x.png) | ![cboy b2 512px](examples/astronaut_cboy_b2_512px_1x.png) | ![cboy b3 512px](examples/astronaut_cboy_b3_512px_1x.png) | ![cboy b4 512px](examples/astronaut_cboy_b4_512px_1x.png) | ![cboy b5 512px](examples/astronaut_cboy_b5_512px_1x.png) |
| *dmg4* | ![dmg4 f 512px](examples/astronaut_dmg4_f_512px_1x.png) | ![dmg4 s 512px](examples/astronaut_dmg4_s_512px_1x.png) | ![dmg4 b1 512px](examples/astronaut_dmg4_b1_512px_1x.png) | ![dmg4 b2 512px](examples/astronaut_dmg4_b2_512px_1x.png) | ![dmg4 b3 512px](examples/astronaut_dmg4_b3_512px_1x.png) | ![dmg4 b4 512px](examples/astronaut_dmg4_b4_512px_1x.png) | ![dmg4 b5 512px](examples/astronaut_dmg4_b5_512px_1x.png) |
| *h16d* | ![h16d f 512px](examples/astronaut_h16d_f_512px_1x.png) | ![h16d s 512px](examples/astronaut_h16d_s_512px_1x.png) | ![h16d b1 512px](examples/astronaut_h16d_b1_512px_1x.png) | ![h16d b2 512px](examples/astronaut_h16d_b2_512px_1x.png) | ![h16d b3 512px](examples/astronaut_h16d_b3_512px_1x.png) | ![h16d b4 512px](examples/astronaut_h16d_b4_512px_1x.png) | ![h16d b5 512px](examples/astronaut_h16d_b5_512px_1x.png) |
| *rdio* | ![rdio f 512px](examples/astronaut_rdio_f_512px_1x.png) | ![rdio s 512px](examples/astronaut_rdio_s_512px_1x.png) | ![rdio b1 512px](examples/astronaut_rdio_b1_512px_1x.png) | ![rdio b2 512px](examples/astronaut_rdio_b2_512px_1x.png) | ![rdio b3 512px](examples/astronaut_rdio_b3_512px_1x.png) | ![rdio b4 512px](examples/astronaut_rdio_b4_512px_1x.png) | ![rdio b5 512px](examples/astronaut_rdio_b5_512px_1x.png) |
| *pstl* | ![pstl f 512px](examples/astronaut_pstl_f_512px_1x.png) | ![pstl s 512px](examples/astronaut_pstl_s_512px_1x.png) | ![pstl b1 512px](examples/astronaut_pstl_b1_512px_1x.png) | ![pstl b2 512px](examples/astronaut_pstl_b2_512px_1x.png) | ![pstl b3 512px](examples/astronaut_pstl_b3_512px_1x.png) | ![pstl b4 512px](examples/astronaut_pstl_b4_512px_1x.png) | ![pstl b5 512px](examples/astronaut_pstl_b5_512px_1x.png) |
| *ayy4* | ![ayy4 f 512px](examples/astronaut_ayy4_f_512px_1x.png) | ![ayy4 s 512px](examples/astronaut_ayy4_s_512px_1x.png) | ![ayy4 b1 512px](examples/astronaut_ayy4_b1_512px_1x.png) | ![ayy4 b2 512px](examples/astronaut_ayy4_b2_512px_1x.png) | ![ayy4 b3 512px](examples/astronaut_ayy4_b3_512px_1x.png) | ![ayy4 b4 512px](examples/astronaut_ayy4_b4_512px_1x.png) | ![ayy4 b5 512px](examples/astronaut_ayy4_b5_512px_1x.png) |
| *2bit* | ![2bit f 512px](examples/astronaut_2bit_f_512px_1x.png) | ![2bit s 512px](examples/astronaut_2bit_s_512px_1x.png) | ![2bit b1 512px](examples/astronaut_2bit_b1_512px_1x.png) | ![2bit b2 512px](examples/astronaut_2bit_b2_512px_1x.png) | ![2bit b3 512px](examples/astronaut_2bit_b3_512px_1x.png) | ![2bit b4 512px](examples/astronaut_2bit_b4_512px_1x.png) | ![2bit b5 512px](examples/astronaut_2bit_b5_512px_1x.png) |
| *cycl* | ![cycl f 512px](examples/astronaut_cycl_f_512px_1x.png) | ![cycl s 512px](examples/astronaut_cycl_s_512px_1x.png) | ![cycl b1 512px](examples/astronaut_cycl_b1_512px_1x.png) | ![cycl b2 512px](examples/astronaut_cycl_b2_512px_1x.png) | ![cycl b3 512px](examples/astronaut_cycl_b3_512px_1x.png) | ![cycl b4 512px](examples/astronaut_cycl_b4_512px_1x.png) | ![cycl b5 512px](examples/astronaut_cycl_b5_512px_1x.png) |
| *cqst* | ![cqst f 512px](examples/astronaut_cqst_f_512px_1x.png) | ![cqst s 512px](examples/astronaut_cqst_s_512px_1x.png) | ![cqst b1 512px](examples/astronaut_cqst_b1_512px_1x.png) | ![cqst b2 512px](examples/astronaut_cqst_b2_512px_1x.png) | ![cqst b3 512px](examples/astronaut_cqst_b3_512px_1x.png) | ![cqst b4 512px](examples/astronaut_cqst_b4_512px_1x.png) | ![cqst b5 512px](examples/astronaut_cqst_b5_512px_1x.png) |
| *cpnk* | ![cpnk f 512px](examples/astronaut_cpnk_f_512px_1x.png) | ![cpnk s 512px](examples/astronaut_cpnk_s_512px_1x.png) | ![cpnk b1 512px](examples/astronaut_cpnk_b1_512px_1x.png) | ![cpnk b2 512px](examples/astronaut_cpnk_b2_512px_1x.png) | ![cpnk b3 512px](examples/astronaut_cpnk_b3_512px_1x.png) | ![cpnk b4 512px](examples/astronaut_cpnk_b4_512px_1x.png) | ![cpnk b5 512px](examples/astronaut_cpnk_b5_512px_1x.png) |
| *exst* | ![exst f 512px](examples/astronaut_exst_f_512px_1x.png) | ![exst s 512px](examples/astronaut_exst_s_512px_1x.png) | ![exst b1 512px](examples/astronaut_exst_b1_512px_1x.png) | ![exst b2 512px](examples/astronaut_exst_b2_512px_1x.png) | ![exst b3 512px](examples/astronaut_exst_b3_512px_1x.png) | ![exst b4 512px](examples/astronaut_exst_b4_512px_1x.png) | ![exst b5 512px](examples/astronaut_exst_b5_512px_1x.png) |
| *hlow* | ![hlow f 512px](examples/astronaut_hlow_f_512px_1x.png) | ![hlow s 512px](examples/astronaut_hlow_s_512px_1x.png) | ![hlow b1 512px](examples/astronaut_hlow_b1_512px_1x.png) | ![hlow b2 512px](examples/astronaut_hlow_b2_512px_1x.png) | ![hlow b3 512px](examples/astronaut_hlow_b3_512px_1x.png) | ![hlow b4 512px](examples/astronaut_hlow_b4_512px_1x.png) | ![hlow b5 512px](examples/astronaut_hlow_b5_512px_1x.png) |
| *kiro* | ![kiro f 512px](examples/astronaut_kiro_f_512px_1x.png) | ![kiro s 512px](examples/astronaut_kiro_s_512px_1x.png) | ![kiro b1 512px](examples/astronaut_kiro_b1_512px_1x.png) | ![kiro b2 512px](examples/astronaut_kiro_b2_512px_1x.png) | ![kiro b3 512px](examples/astronaut_kiro_b3_512px_1x.png) | ![kiro b4 512px](examples/astronaut_kiro_b4_512px_1x.png) | ![kiro b5 512px](examples/astronaut_kiro_b5_512px_1x.png) |
| *mod4* | ![mod4 f 512px](examples/astronaut_mod4_f_512px_1x.png) | ![mod4 s 512px](examples/astronaut_mod4_s_512px_1x.png) | ![mod4 b1 512px](examples/astronaut_mod4_b1_512px_1x.png) | ![mod4 b2 512px](examples/astronaut_mod4_b2_512px_1x.png) | ![mod4 b3 512px](examples/astronaut_mod4_b3_512px_1x.png) | ![mod4 b4 512px](examples/astronaut_mod4_b4_512px_1x.png) | ![mod4 b5 512px](examples/astronaut_mod4_b5_512px_1x.png) |
| *prds* | ![prds f 512px](examples/astronaut_prds_f_512px_1x.png) | ![prds s 512px](examples/astronaut_prds_s_512px_1x.png) | ![prds b1 512px](examples/astronaut_prds_b1_512px_1x.png) | ![prds b2 512px](examples/astronaut_prds_b2_512px_1x.png) | ![prds b3 512px](examples/astronaut_prds_b3_512px_1x.png) | ![prds b4 512px](examples/astronaut_prds_b4_512px_1x.png) | ![prds b5 512px](examples/astronaut_prds_b5_512px_1x.png) |
| *haze* | ![haze f 512px](examples/astronaut_haze_f_512px_1x.png) | ![haze s 512px](examples/astronaut_haze_s_512px_1x.png) | ![haze b1 512px](examples/astronaut_haze_b1_512px_1x.png) | ![haze b2 512px](examples/astronaut_haze_b2_512px_1x.png) | ![haze b3 512px](examples/astronaut_haze_b3_512px_1x.png) | ![haze b4 512px](examples/astronaut_haze_b4_512px_1x.png) | ![haze b5 512px](examples/astronaut_haze_b5_512px_1x.png) |
| *antq* | ![antq f 512px](examples/astronaut_antq_f_512px_1x.png) | ![antq s 512px](examples/astronaut_antq_s_512px_1x.png) | ![antq b1 512px](examples/astronaut_antq_b1_512px_1x.png) | ![antq b2 512px](examples/astronaut_antq_b2_512px_1x.png) | ![antq b3 512px](examples/astronaut_antq_b3_512px_1x.png) | ![antq b4 512px](examples/astronaut_antq_b4_512px_1x.png) | ![antq b5 512px](examples/astronaut_antq_b5_512px_1x.png) |
 
### 256px
 
[Complete Sample Sheet](examples/astronaut_sample_256px_2x.png)
 
| Palette | Floyd | Sierra | Bayer 1 | Bayer 2 | Bayer 3 | Bayer 4 | Bayer 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *default* | ![default f 256px](examples/astronaut_default_f_256px_2x.png) | ![default s 256px](examples/astronaut_default_s_256px_2x.png) | ![default b1 256px](examples/astronaut_default_b1_256px_2x.png) | ![default b2 256px](examples/astronaut_default_b2_256px_2x.png) | ![default b3 256px](examples/astronaut_default_b3_256px_2x.png) | ![default b4 256px](examples/astronaut_default_b4_256px_2x.png) | ![default b5 256px](examples/astronaut_default_b5_256px_2x.png) |
| *nostalgia* | ![nostalgia f 256px](examples/astronaut_nostalgia_f_256px_2x.png) | ![nostalgia s 256px](examples/astronaut_nostalgia_s_256px_2x.png) | ![nostalgia b1 256px](examples/astronaut_nostalgia_b1_256px_2x.png) | ![nostalgia b2 256px](examples/astronaut_nostalgia_b2_256px_2x.png) | ![nostalgia b3 256px](examples/astronaut_nostalgia_b3_256px_2x.png) | ![nostalgia b4 256px](examples/astronaut_nostalgia_b4_256px_2x.png) | ![nostalgia b5 256px](examples/astronaut_nostalgia_b5_256px_2x.png) |
| *cc29* | ![cc29 f 256px](examples/astronaut_cc29_f_256px_2x.png) | ![cc29 s 256px](examples/astronaut_cc29_s_256px_2x.png) | ![cc29 b1 256px](examples/astronaut_cc29_b1_256px_2x.png) | ![cc29 b2 256px](examples/astronaut_cc29_b2_256px_2x.png) | ![cc29 b3 256px](examples/astronaut_cc29_b3_256px_2x.png) | ![cc29 b4 256px](examples/astronaut_cc29_b4_256px_2x.png) | ![cc29 b5 256px](examples/astronaut_cc29_b5_256px_2x.png) |
| *cboy* | ![cboy f 256px](examples/astronaut_cboy_f_256px_2x.png) | ![cboy s 256px](examples/astronaut_cboy_s_256px_2x.png) | ![cboy b1 256px](examples/astronaut_cboy_b1_256px_2x.png) | ![cboy b2 256px](examples/astronaut_cboy_b2_256px_2x.png) | ![cboy b3 256px](examples/astronaut_cboy_b3_256px_2x.png) | ![cboy b4 256px](examples/astronaut_cboy_b4_256px_2x.png) | ![cboy b5 256px](examples/astronaut_cboy_b5_256px_2x.png) |
| *dmg4* | ![dmg4 f 256px](examples/astronaut_dmg4_f_256px_2x.png) | ![dmg4 s 256px](examples/astronaut_dmg4_s_256px_2x.png) | ![dmg4 b1 256px](examples/astronaut_dmg4_b1_256px_2x.png) | ![dmg4 b2 256px](examples/astronaut_dmg4_b2_256px_2x.png) | ![dmg4 b3 256px](examples/astronaut_dmg4_b3_256px_2x.png) | ![dmg4 b4 256px](examples/astronaut_dmg4_b4_256px_2x.png) | ![dmg4 b5 256px](examples/astronaut_dmg4_b5_256px_2x.png) |
| *h16d* | ![h16d f 256px](examples/astronaut_h16d_f_256px_2x.png) | ![h16d s 256px](examples/astronaut_h16d_s_256px_2x.png) | ![h16d b1 256px](examples/astronaut_h16d_b1_256px_2x.png) | ![h16d b2 256px](examples/astronaut_h16d_b2_256px_2x.png) | ![h16d b3 256px](examples/astronaut_h16d_b3_256px_2x.png) | ![h16d b4 256px](examples/astronaut_h16d_b4_256px_2x.png) | ![h16d b5 256px](examples/astronaut_h16d_b5_256px_2x.png) |
| *rdio* | ![rdio f 256px](examples/astronaut_rdio_f_256px_2x.png) | ![rdio s 256px](examples/astronaut_rdio_s_256px_2x.png) | ![rdio b1 256px](examples/astronaut_rdio_b1_256px_2x.png) | ![rdio b2 256px](examples/astronaut_rdio_b2_256px_2x.png) | ![rdio b3 256px](examples/astronaut_rdio_b3_256px_2x.png) | ![rdio b4 256px](examples/astronaut_rdio_b4_256px_2x.png) | ![rdio b5 256px](examples/astronaut_rdio_b5_256px_2x.png) |
| *pstl* | ![pstl f 256px](examples/astronaut_pstl_f_256px_2x.png) | ![pstl s 256px](examples/astronaut_pstl_s_256px_2x.png) | ![pstl b1 256px](examples/astronaut_pstl_b1_256px_2x.png) | ![pstl b2 256px](examples/astronaut_pstl_b2_256px_2x.png) | ![pstl b3 256px](examples/astronaut_pstl_b3_256px_2x.png) | ![pstl b4 256px](examples/astronaut_pstl_b4_256px_2x.png) | ![pstl b5 256px](examples/astronaut_pstl_b5_256px_2x.png) |
| *ayy4* | ![ayy4 f 256px](examples/astronaut_ayy4_f_256px_2x.png) | ![ayy4 s 256px](examples/astronaut_ayy4_s_256px_2x.png) | ![ayy4 b1 256px](examples/astronaut_ayy4_b1_256px_2x.png) | ![ayy4 b2 256px](examples/astronaut_ayy4_b2_256px_2x.png) | ![ayy4 b3 256px](examples/astronaut_ayy4_b3_256px_2x.png) | ![ayy4 b4 256px](examples/astronaut_ayy4_b4_256px_2x.png) | ![ayy4 b5 256px](examples/astronaut_ayy4_b5_256px_2x.png) |
| *2bit* | ![2bit f 256px](examples/astronaut_2bit_f_256px_2x.png) | ![2bit s 256px](examples/astronaut_2bit_s_256px_2x.png) | ![2bit b1 256px](examples/astronaut_2bit_b1_256px_2x.png) | ![2bit b2 256px](examples/astronaut_2bit_b2_256px_2x.png) | ![2bit b3 256px](examples/astronaut_2bit_b3_256px_2x.png) | ![2bit b4 256px](examples/astronaut_2bit_b4_256px_2x.png) | ![2bit b5 256px](examples/astronaut_2bit_b5_256px_2x.png) |
| *cycl* | ![cycl f 256px](examples/astronaut_cycl_f_256px_2x.png) | ![cycl s 256px](examples/astronaut_cycl_s_256px_2x.png) | ![cycl b1 256px](examples/astronaut_cycl_b1_256px_2x.png) | ![cycl b2 256px](examples/astronaut_cycl_b2_256px_2x.png) | ![cycl b3 256px](examples/astronaut_cycl_b3_256px_2x.png) | ![cycl b4 256px](examples/astronaut_cycl_b4_256px_2x.png) | ![cycl b5 256px](examples/astronaut_cycl_b5_256px_2x.png) |
| *cqst* | ![cqst f 256px](examples/astronaut_cqst_f_256px_2x.png) | ![cqst s 256px](examples/astronaut_cqst_s_256px_2x.png) | ![cqst b1 256px](examples/astronaut_cqst_b1_256px_2x.png) | ![cqst b2 256px](examples/astronaut_cqst_b2_256px_2x.png) | ![cqst b3 256px](examples/astronaut_cqst_b3_256px_2x.png) | ![cqst b4 256px](examples/astronaut_cqst_b4_256px_2x.png) | ![cqst b5 256px](examples/astronaut_cqst_b5_256px_2x.png) |
| *cpnk* | ![cpnk f 256px](examples/astronaut_cpnk_f_256px_2x.png) | ![cpnk s 256px](examples/astronaut_cpnk_s_256px_2x.png) | ![cpnk b1 256px](examples/astronaut_cpnk_b1_256px_2x.png) | ![cpnk b2 256px](examples/astronaut_cpnk_b2_256px_2x.png) | ![cpnk b3 256px](examples/astronaut_cpnk_b3_256px_2x.png) | ![cpnk b4 256px](examples/astronaut_cpnk_b4_256px_2x.png) | ![cpnk b5 256px](examples/astronaut_cpnk_b5_256px_2x.png) |
| *exst* | ![exst f 256px](examples/astronaut_exst_f_256px_2x.png) | ![exst s 256px](examples/astronaut_exst_s_256px_2x.png) | ![exst b1 256px](examples/astronaut_exst_b1_256px_2x.png) | ![exst b2 256px](examples/astronaut_exst_b2_256px_2x.png) | ![exst b3 256px](examples/astronaut_exst_b3_256px_2x.png) | ![exst b4 256px](examples/astronaut_exst_b4_256px_2x.png) | ![exst b5 256px](examples/astronaut_exst_b5_256px_2x.png) |
| *hlow* | ![hlow f 256px](examples/astronaut_hlow_f_256px_2x.png) | ![hlow s 256px](examples/astronaut_hlow_s_256px_2x.png) | ![hlow b1 256px](examples/astronaut_hlow_b1_256px_2x.png) | ![hlow b2 256px](examples/astronaut_hlow_b2_256px_2x.png) | ![hlow b3 256px](examples/astronaut_hlow_b3_256px_2x.png) | ![hlow b4 256px](examples/astronaut_hlow_b4_256px_2x.png) | ![hlow b5 256px](examples/astronaut_hlow_b5_256px_2x.png) |
| *kiro* | ![kiro f 256px](examples/astronaut_kiro_f_256px_2x.png) | ![kiro s 256px](examples/astronaut_kiro_s_256px_2x.png) | ![kiro b1 256px](examples/astronaut_kiro_b1_256px_2x.png) | ![kiro b2 256px](examples/astronaut_kiro_b2_256px_2x.png) | ![kiro b3 256px](examples/astronaut_kiro_b3_256px_2x.png) | ![kiro b4 256px](examples/astronaut_kiro_b4_256px_2x.png) | ![kiro b5 256px](examples/astronaut_kiro_b5_256px_2x.png) |
| *mod4* | ![mod4 f 256px](examples/astronaut_mod4_f_256px_2x.png) | ![mod4 s 256px](examples/astronaut_mod4_s_256px_2x.png) | ![mod4 b1 256px](examples/astronaut_mod4_b1_256px_2x.png) | ![mod4 b2 256px](examples/astronaut_mod4_b2_256px_2x.png) | ![mod4 b3 256px](examples/astronaut_mod4_b3_256px_2x.png) | ![mod4 b4 256px](examples/astronaut_mod4_b4_256px_2x.png) | ![mod4 b5 256px](examples/astronaut_mod4_b5_256px_2x.png) |
| *prds* | ![prds f 256px](examples/astronaut_prds_f_256px_2x.png) | ![prds s 256px](examples/astronaut_prds_s_256px_2x.png) | ![prds b1 256px](examples/astronaut_prds_b1_256px_2x.png) | ![prds b2 256px](examples/astronaut_prds_b2_256px_2x.png) | ![prds b3 256px](examples/astronaut_prds_b3_256px_2x.png) | ![prds b4 256px](examples/astronaut_prds_b4_256px_2x.png) | ![prds b5 256px](examples/astronaut_prds_b5_256px_2x.png) |
| *haze* | ![haze f 256px](examples/astronaut_haze_f_256px_2x.png) | ![haze s 256px](examples/astronaut_haze_s_256px_2x.png) | ![haze b1 256px](examples/astronaut_haze_b1_256px_2x.png) | ![haze b2 256px](examples/astronaut_haze_b2_256px_2x.png) | ![haze b3 256px](examples/astronaut_haze_b3_256px_2x.png) | ![haze b4 256px](examples/astronaut_haze_b4_256px_2x.png) | ![haze b5 256px](examples/astronaut_haze_b5_256px_2x.png) |
| *antq* | ![antq f 256px](examples/astronaut_antq_f_256px_2x.png) | ![antq s 256px](examples/astronaut_antq_s_256px_2x.png) | ![antq b1 256px](examples/astronaut_antq_b1_256px_2x.png) | ![antq b2 256px](examples/astronaut_antq_b2_256px_2x.png) | ![antq b3 256px](examples/astronaut_antq_b3_256px_2x.png) | ![antq b4 256px](examples/astronaut_antq_b4_256px_2x.png) | ![antq b5 256px](examples/astronaut_antq_b5_256px_2x.png) |
 
### 128px
 
[Complete Sample Sheet](examples/astronaut_sample_128px_4x.png)
 
| Palette | Floyd | Sierra | Bayer 1 | Bayer 2 | Bayer 3 | Bayer 4 | Bayer 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *default* | ![default f 128px](examples/astronaut_default_f_128px_4x.png) | ![default s 128px](examples/astronaut_default_s_128px_4x.png) | ![default b1 128px](examples/astronaut_default_b1_128px_4x.png) | ![default b2 128px](examples/astronaut_default_b2_128px_4x.png) | ![default b3 128px](examples/astronaut_default_b3_128px_4x.png) | ![default b4 128px](examples/astronaut_default_b4_128px_4x.png) | ![default b5 128px](examples/astronaut_default_b5_128px_4x.png) |
| *nostalgia* | ![nostalgia f 128px](examples/astronaut_nostalgia_f_128px_4x.png) | ![nostalgia s 128px](examples/astronaut_nostalgia_s_128px_4x.png) | ![nostalgia b1 128px](examples/astronaut_nostalgia_b1_128px_4x.png) | ![nostalgia b2 128px](examples/astronaut_nostalgia_b2_128px_4x.png) | ![nostalgia b3 128px](examples/astronaut_nostalgia_b3_128px_4x.png) | ![nostalgia b4 128px](examples/astronaut_nostalgia_b4_128px_4x.png) | ![nostalgia b5 128px](examples/astronaut_nostalgia_b5_128px_4x.png) |
| *cc29* | ![cc29 f 128px](examples/astronaut_cc29_f_128px_4x.png) | ![cc29 s 128px](examples/astronaut_cc29_s_128px_4x.png) | ![cc29 b1 128px](examples/astronaut_cc29_b1_128px_4x.png) | ![cc29 b2 128px](examples/astronaut_cc29_b2_128px_4x.png) | ![cc29 b3 128px](examples/astronaut_cc29_b3_128px_4x.png) | ![cc29 b4 128px](examples/astronaut_cc29_b4_128px_4x.png) | ![cc29 b5 128px](examples/astronaut_cc29_b5_128px_4x.png) |
| *cboy* | ![cboy f 128px](examples/astronaut_cboy_f_128px_4x.png) | ![cboy s 128px](examples/astronaut_cboy_s_128px_4x.png) | ![cboy b1 128px](examples/astronaut_cboy_b1_128px_4x.png) | ![cboy b2 128px](examples/astronaut_cboy_b2_128px_4x.png) | ![cboy b3 128px](examples/astronaut_cboy_b3_128px_4x.png) | ![cboy b4 128px](examples/astronaut_cboy_b4_128px_4x.png) | ![cboy b5 128px](examples/astronaut_cboy_b5_128px_4x.png) |
| *dmg4* | ![dmg4 f 128px](examples/astronaut_dmg4_f_128px_4x.png) | ![dmg4 s 128px](examples/astronaut_dmg4_s_128px_4x.png) | ![dmg4 b1 128px](examples/astronaut_dmg4_b1_128px_4x.png) | ![dmg4 b2 128px](examples/astronaut_dmg4_b2_128px_4x.png) | ![dmg4 b3 128px](examples/astronaut_dmg4_b3_128px_4x.png) | ![dmg4 b4 128px](examples/astronaut_dmg4_b4_128px_4x.png) | ![dmg4 b5 128px](examples/astronaut_dmg4_b5_128px_4x.png) |
| *h16d* | ![h16d f 128px](examples/astronaut_h16d_f_128px_4x.png) | ![h16d s 128px](examples/astronaut_h16d_s_128px_4x.png) | ![h16d b1 128px](examples/astronaut_h16d_b1_128px_4x.png) | ![h16d b2 128px](examples/astronaut_h16d_b2_128px_4x.png) | ![h16d b3 128px](examples/astronaut_h16d_b3_128px_4x.png) | ![h16d b4 128px](examples/astronaut_h16d_b4_128px_4x.png) | ![h16d b5 128px](examples/astronaut_h16d_b5_128px_4x.png) |
| *rdio* | ![rdio f 128px](examples/astronaut_rdio_f_128px_4x.png) | ![rdio s 128px](examples/astronaut_rdio_s_128px_4x.png) | ![rdio b1 128px](examples/astronaut_rdio_b1_128px_4x.png) | ![rdio b2 128px](examples/astronaut_rdio_b2_128px_4x.png) | ![rdio b3 128px](examples/astronaut_rdio_b3_128px_4x.png) | ![rdio b4 128px](examples/astronaut_rdio_b4_128px_4x.png) | ![rdio b5 128px](examples/astronaut_rdio_b5_128px_4x.png) |
| *pstl* | ![pstl f 128px](examples/astronaut_pstl_f_128px_4x.png) | ![pstl s 128px](examples/astronaut_pstl_s_128px_4x.png) | ![pstl b1 128px](examples/astronaut_pstl_b1_128px_4x.png) | ![pstl b2 128px](examples/astronaut_pstl_b2_128px_4x.png) | ![pstl b3 128px](examples/astronaut_pstl_b3_128px_4x.png) | ![pstl b4 128px](examples/astronaut_pstl_b4_128px_4x.png) | ![pstl b5 128px](examples/astronaut_pstl_b5_128px_4x.png) |
| *ayy4* | ![ayy4 f 128px](examples/astronaut_ayy4_f_128px_4x.png) | ![ayy4 s 128px](examples/astronaut_ayy4_s_128px_4x.png) | ![ayy4 b1 128px](examples/astronaut_ayy4_b1_128px_4x.png) | ![ayy4 b2 128px](examples/astronaut_ayy4_b2_128px_4x.png) | ![ayy4 b3 128px](examples/astronaut_ayy4_b3_128px_4x.png) | ![ayy4 b4 128px](examples/astronaut_ayy4_b4_128px_4x.png) | ![ayy4 b5 128px](examples/astronaut_ayy4_b5_128px_4x.png) |
| *2bit* | ![2bit f 128px](examples/astronaut_2bit_f_128px_4x.png) | ![2bit s 128px](examples/astronaut_2bit_s_128px_4x.png) | ![2bit b1 128px](examples/astronaut_2bit_b1_128px_4x.png) | ![2bit b2 128px](examples/astronaut_2bit_b2_128px_4x.png) | ![2bit b3 128px](examples/astronaut_2bit_b3_128px_4x.png) | ![2bit b4 128px](examples/astronaut_2bit_b4_128px_4x.png) | ![2bit b5 128px](examples/astronaut_2bit_b5_128px_4x.png) |
| *cycl* | ![cycl f 128px](examples/astronaut_cycl_f_128px_4x.png) | ![cycl s 128px](examples/astronaut_cycl_s_128px_4x.png) | ![cycl b1 128px](examples/astronaut_cycl_b1_128px_4x.png) | ![cycl b2 128px](examples/astronaut_cycl_b2_128px_4x.png) | ![cycl b3 128px](examples/astronaut_cycl_b3_128px_4x.png) | ![cycl b4 128px](examples/astronaut_cycl_b4_128px_4x.png) | ![cycl b5 128px](examples/astronaut_cycl_b5_128px_4x.png) |
| *cqst* | ![cqst f 128px](examples/astronaut_cqst_f_128px_4x.png) | ![cqst s 128px](examples/astronaut_cqst_s_128px_4x.png) | ![cqst b1 128px](examples/astronaut_cqst_b1_128px_4x.png) | ![cqst b2 128px](examples/astronaut_cqst_b2_128px_4x.png) | ![cqst b3 128px](examples/astronaut_cqst_b3_128px_4x.png) | ![cqst b4 128px](examples/astronaut_cqst_b4_128px_4x.png) | ![cqst b5 128px](examples/astronaut_cqst_b5_128px_4x.png) |
| *cpnk* | ![cpnk f 128px](examples/astronaut_cpnk_f_128px_4x.png) | ![cpnk s 128px](examples/astronaut_cpnk_s_128px_4x.png) | ![cpnk b1 128px](examples/astronaut_cpnk_b1_128px_4x.png) | ![cpnk b2 128px](examples/astronaut_cpnk_b2_128px_4x.png) | ![cpnk b3 128px](examples/astronaut_cpnk_b3_128px_4x.png) | ![cpnk b4 128px](examples/astronaut_cpnk_b4_128px_4x.png) | ![cpnk b5 128px](examples/astronaut_cpnk_b5_128px_4x.png) |
| *exst* | ![exst f 128px](examples/astronaut_exst_f_128px_4x.png) | ![exst s 128px](examples/astronaut_exst_s_128px_4x.png) | ![exst b1 128px](examples/astronaut_exst_b1_128px_4x.png) | ![exst b2 128px](examples/astronaut_exst_b2_128px_4x.png) | ![exst b3 128px](examples/astronaut_exst_b3_128px_4x.png) | ![exst b4 128px](examples/astronaut_exst_b4_128px_4x.png) | ![exst b5 128px](examples/astronaut_exst_b5_128px_4x.png) |
| *hlow* | ![hlow f 128px](examples/astronaut_hlow_f_128px_4x.png) | ![hlow s 128px](examples/astronaut_hlow_s_128px_4x.png) | ![hlow b1 128px](examples/astronaut_hlow_b1_128px_4x.png) | ![hlow b2 128px](examples/astronaut_hlow_b2_128px_4x.png) | ![hlow b3 128px](examples/astronaut_hlow_b3_128px_4x.png) | ![hlow b4 128px](examples/astronaut_hlow_b4_128px_4x.png) | ![hlow b5 128px](examples/astronaut_hlow_b5_128px_4x.png) |
| *kiro* | ![kiro f 128px](examples/astronaut_kiro_f_128px_4x.png) | ![kiro s 128px](examples/astronaut_kiro_s_128px_4x.png) | ![kiro b1 128px](examples/astronaut_kiro_b1_128px_4x.png) | ![kiro b2 128px](examples/astronaut_kiro_b2_128px_4x.png) | ![kiro b3 128px](examples/astronaut_kiro_b3_128px_4x.png) | ![kiro b4 128px](examples/astronaut_kiro_b4_128px_4x.png) | ![kiro b5 128px](examples/astronaut_kiro_b5_128px_4x.png) |
| *mod4* | ![mod4 f 128px](examples/astronaut_mod4_f_128px_4x.png) | ![mod4 s 128px](examples/astronaut_mod4_s_128px_4x.png) | ![mod4 b1 128px](examples/astronaut_mod4_b1_128px_4x.png) | ![mod4 b2 128px](examples/astronaut_mod4_b2_128px_4x.png) | ![mod4 b3 128px](examples/astronaut_mod4_b3_128px_4x.png) | ![mod4 b4 128px](examples/astronaut_mod4_b4_128px_4x.png) | ![mod4 b5 128px](examples/astronaut_mod4_b5_128px_4x.png) |
| *prds* | ![prds f 128px](examples/astronaut_prds_f_128px_4x.png) | ![prds s 128px](examples/astronaut_prds_s_128px_4x.png) | ![prds b1 128px](examples/astronaut_prds_b1_128px_4x.png) | ![prds b2 128px](examples/astronaut_prds_b2_128px_4x.png) | ![prds b3 128px](examples/astronaut_prds_b3_128px_4x.png) | ![prds b4 128px](examples/astronaut_prds_b4_128px_4x.png) | ![prds b5 128px](examples/astronaut_prds_b5_128px_4x.png) |
| *haze* | ![haze f 128px](examples/astronaut_haze_f_128px_4x.png) | ![haze s 128px](examples/astronaut_haze_s_128px_4x.png) | ![haze b1 128px](examples/astronaut_haze_b1_128px_4x.png) | ![haze b2 128px](examples/astronaut_haze_b2_128px_4x.png) | ![haze b3 128px](examples/astronaut_haze_b3_128px_4x.png) | ![haze b4 128px](examples/astronaut_haze_b4_128px_4x.png) | ![haze b5 128px](examples/astronaut_haze_b5_128px_4x.png) |
| *antq* | ![antq f 128px](examples/astronaut_antq_f_128px_4x.png) | ![antq s 128px](examples/astronaut_antq_s_128px_4x.png) | ![antq b1 128px](examples/astronaut_antq_b1_128px_4x.png) | ![antq b2 128px](examples/astronaut_antq_b2_128px_4x.png) | ![antq b3 128px](examples/astronaut_antq_b3_128px_4x.png) | ![antq b4 128px](examples/astronaut_antq_b4_128px_4x.png) | ![antq b5 128px](examples/astronaut_antq_b5_128px_4x.png) |
 
### 64px
 
[Complete Sample Sheet](examples/astronaut_sample_64px_8x.png)
 
| Palette | Floyd | Sierra | Bayer 1 | Bayer 2 | Bayer 3 | Bayer 4 | Bayer 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *default* | ![default f 64px](examples/astronaut_default_f_64px_8x.png) | ![default s 64px](examples/astronaut_default_s_64px_8x.png) | ![default b1 64px](examples/astronaut_default_b1_64px_8x.png) | ![default b2 64px](examples/astronaut_default_b2_64px_8x.png) | ![default b3 64px](examples/astronaut_default_b3_64px_8x.png) | ![default b4 64px](examples/astronaut_default_b4_64px_8x.png) | ![default b5 64px](examples/astronaut_default_b5_64px_8x.png) |
| *nostalgia* | ![nostalgia f 64px](examples/astronaut_nostalgia_f_64px_8x.png) | ![nostalgia s 64px](examples/astronaut_nostalgia_s_64px_8x.png) | ![nostalgia b1 64px](examples/astronaut_nostalgia_b1_64px_8x.png) | ![nostalgia b2 64px](examples/astronaut_nostalgia_b2_64px_8x.png) | ![nostalgia b3 64px](examples/astronaut_nostalgia_b3_64px_8x.png) | ![nostalgia b4 64px](examples/astronaut_nostalgia_b4_64px_8x.png) | ![nostalgia b5 64px](examples/astronaut_nostalgia_b5_64px_8x.png) |
| *cc29* | ![cc29 f 64px](examples/astronaut_cc29_f_64px_8x.png) | ![cc29 s 64px](examples/astronaut_cc29_s_64px_8x.png) | ![cc29 b1 64px](examples/astronaut_cc29_b1_64px_8x.png) | ![cc29 b2 64px](examples/astronaut_cc29_b2_64px_8x.png) | ![cc29 b3 64px](examples/astronaut_cc29_b3_64px_8x.png) | ![cc29 b4 64px](examples/astronaut_cc29_b4_64px_8x.png) | ![cc29 b5 64px](examples/astronaut_cc29_b5_64px_8x.png) |
| *cboy* | ![cboy f 64px](examples/astronaut_cboy_f_64px_8x.png) | ![cboy s 64px](examples/astronaut_cboy_s_64px_8x.png) | ![cboy b1 64px](examples/astronaut_cboy_b1_64px_8x.png) | ![cboy b2 64px](examples/astronaut_cboy_b2_64px_8x.png) | ![cboy b3 64px](examples/astronaut_cboy_b3_64px_8x.png) | ![cboy b4 64px](examples/astronaut_cboy_b4_64px_8x.png) | ![cboy b5 64px](examples/astronaut_cboy_b5_64px_8x.png) |
| *dmg4* | ![dmg4 f 64px](examples/astronaut_dmg4_f_64px_8x.png) | ![dmg4 s 64px](examples/astronaut_dmg4_s_64px_8x.png) | ![dmg4 b1 64px](examples/astronaut_dmg4_b1_64px_8x.png) | ![dmg4 b2 64px](examples/astronaut_dmg4_b2_64px_8x.png) | ![dmg4 b3 64px](examples/astronaut_dmg4_b3_64px_8x.png) | ![dmg4 b4 64px](examples/astronaut_dmg4_b4_64px_8x.png) | ![dmg4 b5 64px](examples/astronaut_dmg4_b5_64px_8x.png) |
| *h16d* | ![h16d f 64px](examples/astronaut_h16d_f_64px_8x.png) | ![h16d s 64px](examples/astronaut_h16d_s_64px_8x.png) | ![h16d b1 64px](examples/astronaut_h16d_b1_64px_8x.png) | ![h16d b2 64px](examples/astronaut_h16d_b2_64px_8x.png) | ![h16d b3 64px](examples/astronaut_h16d_b3_64px_8x.png) | ![h16d b4 64px](examples/astronaut_h16d_b4_64px_8x.png) | ![h16d b5 64px](examples/astronaut_h16d_b5_64px_8x.png) |
| *rdio* | ![rdio f 64px](examples/astronaut_rdio_f_64px_8x.png) | ![rdio s 64px](examples/astronaut_rdio_s_64px_8x.png) | ![rdio b1 64px](examples/astronaut_rdio_b1_64px_8x.png) | ![rdio b2 64px](examples/astronaut_rdio_b2_64px_8x.png) | ![rdio b3 64px](examples/astronaut_rdio_b3_64px_8x.png) | ![rdio b4 64px](examples/astronaut_rdio_b4_64px_8x.png) | ![rdio b5 64px](examples/astronaut_rdio_b5_64px_8x.png) |
| *pstl* | ![pstl f 64px](examples/astronaut_pstl_f_64px_8x.png) | ![pstl s 64px](examples/astronaut_pstl_s_64px_8x.png) | ![pstl b1 64px](examples/astronaut_pstl_b1_64px_8x.png) | ![pstl b2 64px](examples/astronaut_pstl_b2_64px_8x.png) | ![pstl b3 64px](examples/astronaut_pstl_b3_64px_8x.png) | ![pstl b4 64px](examples/astronaut_pstl_b4_64px_8x.png) | ![pstl b5 64px](examples/astronaut_pstl_b5_64px_8x.png) |
| *ayy4* | ![ayy4 f 64px](examples/astronaut_ayy4_f_64px_8x.png) | ![ayy4 s 64px](examples/astronaut_ayy4_s_64px_8x.png) | ![ayy4 b1 64px](examples/astronaut_ayy4_b1_64px_8x.png) | ![ayy4 b2 64px](examples/astronaut_ayy4_b2_64px_8x.png) | ![ayy4 b3 64px](examples/astronaut_ayy4_b3_64px_8x.png) | ![ayy4 b4 64px](examples/astronaut_ayy4_b4_64px_8x.png) | ![ayy4 b5 64px](examples/astronaut_ayy4_b5_64px_8x.png) |
| *2bit* | ![2bit f 64px](examples/astronaut_2bit_f_64px_8x.png) | ![2bit s 64px](examples/astronaut_2bit_s_64px_8x.png) | ![2bit b1 64px](examples/astronaut_2bit_b1_64px_8x.png) | ![2bit b2 64px](examples/astronaut_2bit_b2_64px_8x.png) | ![2bit b3 64px](examples/astronaut_2bit_b3_64px_8x.png) | ![2bit b4 64px](examples/astronaut_2bit_b4_64px_8x.png) | ![2bit b5 64px](examples/astronaut_2bit_b5_64px_8x.png) |
| *cycl* | ![cycl f 64px](examples/astronaut_cycl_f_64px_8x.png) | ![cycl s 64px](examples/astronaut_cycl_s_64px_8x.png) | ![cycl b1 64px](examples/astronaut_cycl_b1_64px_8x.png) | ![cycl b2 64px](examples/astronaut_cycl_b2_64px_8x.png) | ![cycl b3 64px](examples/astronaut_cycl_b3_64px_8x.png) | ![cycl b4 64px](examples/astronaut_cycl_b4_64px_8x.png) | ![cycl b5 64px](examples/astronaut_cycl_b5_64px_8x.png) |
| *cqst* | ![cqst f 64px](examples/astronaut_cqst_f_64px_8x.png) | ![cqst s 64px](examples/astronaut_cqst_s_64px_8x.png) | ![cqst b1 64px](examples/astronaut_cqst_b1_64px_8x.png) | ![cqst b2 64px](examples/astronaut_cqst_b2_64px_8x.png) | ![cqst b3 64px](examples/astronaut_cqst_b3_64px_8x.png) | ![cqst b4 64px](examples/astronaut_cqst_b4_64px_8x.png) | ![cqst b5 64px](examples/astronaut_cqst_b5_64px_8x.png) |
| *cpnk* | ![cpnk f 64px](examples/astronaut_cpnk_f_64px_8x.png) | ![cpnk s 64px](examples/astronaut_cpnk_s_64px_8x.png) | ![cpnk b1 64px](examples/astronaut_cpnk_b1_64px_8x.png) | ![cpnk b2 64px](examples/astronaut_cpnk_b2_64px_8x.png) | ![cpnk b3 64px](examples/astronaut_cpnk_b3_64px_8x.png) | ![cpnk b4 64px](examples/astronaut_cpnk_b4_64px_8x.png) | ![cpnk b5 64px](examples/astronaut_cpnk_b5_64px_8x.png) |
| *exst* | ![exst f 64px](examples/astronaut_exst_f_64px_8x.png) | ![exst s 64px](examples/astronaut_exst_s_64px_8x.png) | ![exst b1 64px](examples/astronaut_exst_b1_64px_8x.png) | ![exst b2 64px](examples/astronaut_exst_b2_64px_8x.png) | ![exst b3 64px](examples/astronaut_exst_b3_64px_8x.png) | ![exst b4 64px](examples/astronaut_exst_b4_64px_8x.png) | ![exst b5 64px](examples/astronaut_exst_b5_64px_8x.png) |
| *hlow* | ![hlow f 64px](examples/astronaut_hlow_f_64px_8x.png) | ![hlow s 64px](examples/astronaut_hlow_s_64px_8x.png) | ![hlow b1 64px](examples/astronaut_hlow_b1_64px_8x.png) | ![hlow b2 64px](examples/astronaut_hlow_b2_64px_8x.png) | ![hlow b3 64px](examples/astronaut_hlow_b3_64px_8x.png) | ![hlow b4 64px](examples/astronaut_hlow_b4_64px_8x.png) | ![hlow b5 64px](examples/astronaut_hlow_b5_64px_8x.png) |
| *kiro* | ![kiro f 64px](examples/astronaut_kiro_f_64px_8x.png) | ![kiro s 64px](examples/astronaut_kiro_s_64px_8x.png) | ![kiro b1 64px](examples/astronaut_kiro_b1_64px_8x.png) | ![kiro b2 64px](examples/astronaut_kiro_b2_64px_8x.png) | ![kiro b3 64px](examples/astronaut_kiro_b3_64px_8x.png) | ![kiro b4 64px](examples/astronaut_kiro_b4_64px_8x.png) | ![kiro b5 64px](examples/astronaut_kiro_b5_64px_8x.png) |
| *mod4* | ![mod4 f 64px](examples/astronaut_mod4_f_64px_8x.png) | ![mod4 s 64px](examples/astronaut_mod4_s_64px_8x.png) | ![mod4 b1 64px](examples/astronaut_mod4_b1_64px_8x.png) | ![mod4 b2 64px](examples/astronaut_mod4_b2_64px_8x.png) | ![mod4 b3 64px](examples/astronaut_mod4_b3_64px_8x.png) | ![mod4 b4 64px](examples/astronaut_mod4_b4_64px_8x.png) | ![mod4 b5 64px](examples/astronaut_mod4_b5_64px_8x.png) |
| *prds* | ![prds f 64px](examples/astronaut_prds_f_64px_8x.png) | ![prds s 64px](examples/astronaut_prds_s_64px_8x.png) | ![prds b1 64px](examples/astronaut_prds_b1_64px_8x.png) | ![prds b2 64px](examples/astronaut_prds_b2_64px_8x.png) | ![prds b3 64px](examples/astronaut_prds_b3_64px_8x.png) | ![prds b4 64px](examples/astronaut_prds_b4_64px_8x.png) | ![prds b5 64px](examples/astronaut_prds_b5_64px_8x.png) |
| *haze* | ![haze f 64px](examples/astronaut_haze_f_64px_8x.png) | ![haze s 64px](examples/astronaut_haze_s_64px_8x.png) | ![haze b1 64px](examples/astronaut_haze_b1_64px_8x.png) | ![haze b2 64px](examples/astronaut_haze_b2_64px_8x.png) | ![haze b3 64px](examples/astronaut_haze_b3_64px_8x.png) | ![haze b4 64px](examples/astronaut_haze_b4_64px_8x.png) | ![haze b5 64px](examples/astronaut_haze_b5_64px_8x.png) |
| *antq* | ![antq f 64px](examples/astronaut_antq_f_64px_8x.png) | ![antq s 64px](examples/astronaut_antq_s_64px_8x.png) | ![antq b1 64px](examples/astronaut_antq_b1_64px_8x.png) | ![antq b2 64px](examples/astronaut_antq_b2_64px_8x.png) | ![antq b3 64px](examples/astronaut_antq_b3_64px_8x.png) | ![antq b4 64px](examples/astronaut_antq_b4_64px_8x.png) | ![antq b5 64px](examples/astronaut_antq_b5_64px_8x.png) |