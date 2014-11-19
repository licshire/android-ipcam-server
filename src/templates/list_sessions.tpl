%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<p>Active sessions:</p>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Server url</th>
        <th>Content</th>
        <th>Actions</th>
    </tr>

    %for row in active:
    <tr>
        %for col in row:
        <td>{{col}}</td>
        %end
        <td><a href="/rest/session/{{row[0]}}/play">start stream</a></td>
    </tr>
    %end
</table>

<p>Expired sessions:</p>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Server url</th>
        <th>Content</th>
    </tr>

    %for row in expired:
    <tr>
        %for col in row:
        <td>{{col}}</td>
        %end
    </tr>
    %end
</table>
