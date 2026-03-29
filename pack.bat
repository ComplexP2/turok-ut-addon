REM Executing this script automates packing the mod files to kpf
REM This file is supposed to be placed at <TurokRoot>/mods/<ModFolder>/
REM where <ModFolder> contains the local mod files
REM The kpf will be placed at <TurokRoot>/mods/
@echo off
set args=-a -cf "TurokUTAddOn.zip"
set args=%args% -C "." "UTAddOn\*"
set args=%args% -C "." "scripts\*"
set args=%args% -C "." "defs\*"
set args=%args% -C "." "gfx\*"
set args=%args% -C "." "models\*"
set args=%args% -C "." "*.bat"

tar.exe %args%

move TurokUTAddOn.zip ../TurokUTAddOn.kpf
