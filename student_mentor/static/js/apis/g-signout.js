function signOut() 
{
	var auth2 = gapi.auth2.getAuthInstance();
	auth2.signOut()
	.then(function () 
		{
			$.post('http://localhost:8000/home/', {query: 'signout', csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value})
			.done(function()
				{
					window.location.href='http://localhost:8000/';
				}
			);
		}
	);
}
function onLoad() 
{
	gapi.load('auth2', function() 
		{
			gapi.auth2.init();
		}
	);
}
