<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { theme } from "../stores/settings.ts";
  import Button from "../shared/Button.svelte";

  let dispatch = createEventDispatcher();
</script>

<header style="--primary_color: {$theme.primary_color}">
  <div class="left">
    <Button
      type="secondary"
      inverse={false}
      on:click={() => dispatch("toggle_sidebar")}>icon</Button
    >
  </div>
  <div class="middle">middle</div>
  <div class="right">right</div>
</header>

<style>
  header {
    display: flex;
    position: fixed;
    justify-content: space-between;
    align-items: center;
    background: var(--primary_color);
    height: 75px;
    width: 100%;
    top: 0;
  }
</style>
