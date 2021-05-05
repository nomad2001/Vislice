<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
</head>
<body>

  <h1>Vislice</h1>
  <h2>Igraš igro:</h2>
  <h3>Si v stanju {{ stanje }}</h3>

  <h3>Pravilni del gesla</h3>
  <h4>{{ igra.pravilni_del_gesla() }}</h4>

  <h3>Nepravilne črke</h3>
  <h4>{{ igra.napacne_crke() }}</h4>

  <h3>Stopnja obešenosti</h3>
  <h4>{{ igra.stevilo_napak() }}</h4>


  <img src="img/{{ igra.stevilo_napak() }}.jpg" alt="obesanje">
  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <img src="img/10.jpg" alt="Stopnja obešanosti">

  <form>
    <label>Vnesi črko:
      <input type="text" name="crka">
    </label>
    <input type="submit">
  </form>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
</body>

</html>