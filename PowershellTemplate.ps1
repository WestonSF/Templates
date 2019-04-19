# Description
# Name of Process
# Parameters
$python = "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3" 
$pythonScript = "C:\Development\Development Templates\PythonTemplate.py"
$arg1 = "Parameter1"
$arg2 = "Parameter2"

# Code
$env:path="$env:Path;$python"
python $pythonScript $arg1 $arg2