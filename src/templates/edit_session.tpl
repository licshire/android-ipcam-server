%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item

<h3>Edit the session with ID = {{no}}</h3>

<form action="/rest/session/{{no}}/edit" method="get">
    <input type="text" name="name"    value="{{old[0]}}" size="100" maxlength="100">

    <input type="text" name="url"     value="{{old[1]}}" size="100" maxlength="1024">

    <input type="text" name="content" value="{{old[2]}}" size="100" maxlength="1024">

    <select name="status">
        <option>active</option>
        <option>expired</option>
    </select>

    <br/>

    <input type="submit" name="save" value="save">
</form>