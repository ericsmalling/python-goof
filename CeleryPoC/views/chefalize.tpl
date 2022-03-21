<h1>Chefalizer!</h1>

<form action="/" method="POST">
    <label>Enter a phrase to Chefalize!</label>
    <br>
    <textarea name="phrase" rows="10" cols="80"></textarea>
    <br>
    <input type="submit">
</form>
<hr/>
<h3>Completed Chefalizations:</h3>
<ul>
%for row in rows:
    <li>{{row["result"]}}<font size="-3"><a href='/edit/{{row["_id"]}}'>edit</a></font></li>
%end
</ul>