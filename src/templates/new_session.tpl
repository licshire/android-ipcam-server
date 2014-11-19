%#template for the form for a new task

<p>Add a new task to the ToDo list:</p>

<form action="/rest/session/register" method="GET">
    <input type="text" size="100" maxlength="100" name="name" />
    <input type="text" size="100" maxlength="1024" name="url" />
    <input type="text" size="100" maxlength="1024" name="content" />
    <input type="submit" name="save" value="save" />
</form>