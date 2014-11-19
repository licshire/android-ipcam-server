<!doctype html>
<html>

	<head>
		<title>List of sessions</title>

		<meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1.0, user-scalable=yes">

		<script src="/components/platform/platform.js"></script>

		<link rel="import" href="/components/font-roboto/roboto.html">
		<link rel="import" href="/components/core-header-panel/core-header-panel.html">
		<link rel="import" href="/components/core-toolbar/core-toolbar.html">
		<link rel="import" href="/components/paper-tabs/paper-tabs.html">
		<link rel="import" href="/custom-components/session-list.html">

		<style>
			html, body {
				height: 100%;
				margin: 0;
				background-color: #E5E5E5;
				font-family: 'RobotoDraft', sans-serif;
			}
			core-header-panel {
				height: 100%;
				overflow: auto;
				-webkit-overflow-scrolling: touch; 
			}
			core-toolbar {
				background: #03a9f4;
				color: white;
			}
			#tabs {
				width: 100%;
				margin: 0;
				-webkit-user-select: none;
				-moz-user-select: none;
				-ms-user-select: none;
				user-select: none;
				text-transform: uppercase;
			}
			.container {
				width: 80%;
				margin: 50px auto;
			}
			@media (min-width: 481px) {
				#tabs {
					width: 400px;
				}
				.container {
					width: 400px;
				}
			}
		</style>
	</head>

	<body unresolved>
		<core-header-panel>
			<core-toolbar>
				<div flex>List of sessions</div>
				<paper-tabs id="tabs" selected="active" self-end>
					<paper-tab name="active">Active</paper-tab>
					<paper-tab name="expired">Expired</paper-tab>
				</paper-tabs>
			</core-toolbar>
			
			<div class="container" layout vertical center>
				<session-list show="active"></session-list>
			</div>

			<!-- main page content will go here --> 

		</core-header-panel>
		
		<script>
			var tabs = document.querySelector('paper-tabs');
			var list = document.querySelector('session-list');

			tabs.addEventListener('core-select', function() {
				list.show = tabs.selected;
			});
			
		</script>
	</body>
</html>
