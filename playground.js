document.write(`
    <!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PyScript Playground</title>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  <style>
    body {
      background-color: #eee;
    }
    .container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: minmax(200px, auto);
      grid-gap: 1em;
      margin-top: 1em;
    }
    .container > div:first-child {
      grid-row: 1/3;
    }
    .container > div {
      background-color: #fff;
      box-shadow: 0px 5px 10px #ccc;
      padding: 10px;
    }

    #errors {
       color: white;
    }
  </style>
  <py-env>
    - matplotlib
    - numpy
  </py-env>
</head>
<body>
  <div class="container">
    <div>
      <py-repl std-out="output" std-err="errors"></py-repl>
    </div>
    <div>
      <b>Output</b><hr>
      <div id="output">
        <div id='fruits-container'>
            <div class='fruit' id="fruit-1" pys-onClick="show_fruit">🍪</div>
            <div class='fruit' id="fruit-2">🍪</div>
            <div class='fruit' id="fruit-3">🍪</div>
          </div>
         
            <h2 id='exercise'>Exercise: Try turning the cookie into a strawberry! Hint: The left most cookie has an id of <code>fruit-1</code>. Use <code>replaceFruit(div_id, yourFruit)</code></h2>
</div>
    </div>
    <div style='display:none'>
      <b>Errors and Warnings</b><hr>
      <div id="errors"></div>
    </div>
  </div>
</body>
</html>
`);