<script lang="ts">
  import Header from "./components/Header.svelte";

  let sidebar_active: boolean = false;
</script>

<Header />
<main>
  <div class="panels">
    {#if { sidebar_active }}
      <div class="sidebar">sidebar goes here</div>
    {/if}
    <div class="current_chat">Current chat panel should be here.</div>
    <div class="extras_panel">
      Info about person or some other buttons might go here.
    </div>
  </div>
</main>

<style>
  main {
    margin-top: 75px;
    padding: 0;
    width: 100%;
    height: 1000px;
  }
  .panels {
    display: flex;
    justify-content: space-between;
    height: 100%;
  }
  .sidebar {
    width: 25%;
    background-color: red;
  }
  .current_chat {
    width: 100%;
    background-color: green;
  }
  .extras_panel {
    width: 25%;
    background-color: blue;
  }
</style>
