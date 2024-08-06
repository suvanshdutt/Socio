<main>
  <div class="title">
    <h1>
      Socio
    </h1>
  </div>

  <div class="row">
    <div class="column-left">
      <p>something</p>
    </div>

    <div class="column-right">
      <p>something else</p>
    </div>

  </div>
</main>






<style>
  .title{
    height: 72px;
    background-color: rgba(255,255,255,1);
    
  }

  .column-left{
    float: left;
    width: 35%;
    height: 600px;
    background-color: aqua;
  }

  .column-right{
    float: right;
    width: 65%;
    height: 600px;
    background-color: beige;
  }

  .row:after {
    content: "";
    display: table;
    clear: both;
  }
</style>