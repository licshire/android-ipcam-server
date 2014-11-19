<h1>Session: {{name}}</h1>

<p>id: {{sid}}</p>

<p>url: {{url}}</p>

<h3>Streming</h3>

<object
    classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921"
    codebase="http://downloads.videolan.org/pub/videolan/vlc/latest/win32/axvlc.cab"
    width="400" height="300"
    id="vlc" events="True">
    
    <param name="Src" value="{{url}}"></param>
    <param name="ShowDisplay" value="True" ></param>
    <param name="AutoLoop" value="no"></param>
    <param name="AutoPlay" value="yes"></param>
    <embed type="application/x-google-vlc-plugin" name="vlcfirefox" autoplay="yes" loop="no" width="400" height="300" target="{{url}}"></embed>
</object>

<h3>Additional session description</h3>

<p>{{content}}</p>
