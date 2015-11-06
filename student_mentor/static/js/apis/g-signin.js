function onSignIn(googleUser) 
{
	var profile = googleUser.getBasicProfile();
	var id_token = googleUser.getAuthResponse().id_token;
	//alert(id_token);
	console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	console.log('Name: ' + profile.getName());
	console.log('Image URL: ' + profile.getImageUrl());
	console.log('Email: ' + profile.getEmail());
	$.post('http://localhost:8000/check_mail/', {csrfmiddlewaretoken: csrf, email: profile.getEmail(), id_token: id_token, name: profile.getName()})
	.done(function(data)
		{
			if(data.data=='OK')
				submit_form('signin_user');
			if(data.data=='Not OK')
				signOut();
		}
	);
}
