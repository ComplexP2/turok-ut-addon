tar.exe -a -cf "TurokUTAddOn.zip" -C "." "UTAddOn\*" -C "." "scripts\*" -C "." "defs\*" -C "." "models\*" "ReadMe.md" "LICENSE"
move TurokUTAddOn.zip ../TurokUTAddOn.kpf
Start "" "../../sobek.exe"
