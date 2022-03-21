<h1>Chefalizer!</h1>

<form action="/edit" method="POST">
    <label>Edit phrasing</label>
    <br>
    <textarea name="phrase" rows="10" cols="80">{{phrase}}</textarea>
    <br>
    <input type="hidden" name="id" value="{{id}}">
    <input type="submit">
</form>
