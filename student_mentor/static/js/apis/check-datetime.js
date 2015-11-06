//var value = "22.05.2013 11:23:22";
// capture all the parts
function check_datetime(value)
{
	var matches = value.match(/^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})$/);
	//alt:
	// value.match(/^(\d{2}).(\d{2}).(\d{4}).(\d{2}).(\d{2}).(\d{2})$/);
	// also matches 22/05/2013 11:23:22 and 22a0592013,11@23a22
	if (matches == null) 
	{
	    alert('Invalid date or time');
	    return false;
	} 
	else
	{
	    // now lets check the date sanity
		var year = parseInt(matches[1], 10);
		var month = parseInt(matches[2], 10) - 1; // months are 0-11
		var day = parseInt(matches[3], 10);
		var hour = parseInt(matches[4], 10);
		var minute = parseInt(matches[5], 10);
		var date = new Date(year, month, day, hour, minute);
		if (date.getFullYear() !== year || date.getMonth() != month || date.getDate() !== day || date.getHours() !== hour || date.getMinutes() !== minute) 
		{
	       		alert('Invalid date or time');
	       		return false;
		} 
		else 
			return true;
	}
}
