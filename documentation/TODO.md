* TODO: function calls by named argument only seems not to work.
	* Reason: We use the arguments *passed* to the function/method for idenification, not the arguments provided *after mixing with defaults* as a kwargs structure.
	* Right now that implies: All arguments specified in `dependArgs` must be present by the caller. Therefore we fail if default arguments are specified right now. Something that should be fixed.












