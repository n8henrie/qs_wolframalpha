on process_text(query)
	(*
	Assumes you've made a keychain entry with service named `wolframalpha` 
	and account named `appid`, otherwise just put your appid here
	*)
	
	set appid to do shell script "security find-generic-password -s wolframalpha -a appid -w"
	
	set response to do shell script "/usr/local/bin/python3 /path/to/qs_wolframalpha/qs_wolframalpha.py " & appid & " " & quoted form of query
	
	return response
end process_text

using terms from application "Quicksilver"
	on get direct types
		return {"NSStringPboardType"}
	end get direct types
	
	on process text query
		try
			set response to process_text(query)
			tell application "Quicksilver" to set selection to response
		on error a number b
			activate
			display dialog a with title "error with your QS action script"
		end try
	end process text
end using terms from

on run
	set query to text returned of (display dialog "What do you want to ask Wolfram Alpha?" default answer "convert 38 mm to in")
	set response to process_text(query)
	display dialog response
end run
