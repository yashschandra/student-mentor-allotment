function signOut() 
{
	if(!(gapi in window))
		window.location.href='http://localhost:8000/signin/';
	if(gapi.auth2 in window)
	{
		var auth2 = gapi.auth2.getAuthInstance();
		auth2.signOut()
		.then(function () 
			{
				window.location.href='http://localhost:8000/signin/';
			}
		);
	}
	else
		window.location.href='http://localhost:8000/signin/';
}
function onLoad() 
{
	gapi.load('auth2', function() 
		{
			gapi.auth2.init();
		}
	);
}
function auto()
{
	idle_request=setTimeout(signOut, 2000);
}
