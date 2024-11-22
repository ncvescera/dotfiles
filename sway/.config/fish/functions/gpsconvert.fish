function gpsconvert
	# display help menu
	if test "$argv[1]" = "-h"
		echo "gpsconvert INPUT_FILE.kmz [OUTPUT_FILE.gpx]"
		echo ""
		echo "   If no OUTPUT_FILE.gpx is given, the output is automatically set to the input name"
		return 0
	end
	
	# check if argv are passed
	if test (count $argv) -lt 1
		set_color red
		echo "Error: provide at least an INPUT file !"
		return 1
	end
	
	# check if Output File is passed
	if test (count $argv) -eq 1
		set outfile (string join '.' (string sub -e -4 $argv[1]) "gpx")
	else
		set outfile $argv[2]
	end
	
	# convert KMZ to GPX
	unzip -p $argv[1] > in.kml | gpsbabel -i kml -f in.kml -o gpx -F "$outfile"
	rm in.kml	# remove temp file
	
	set_color green
	echo "Done !"
	return 0
end
