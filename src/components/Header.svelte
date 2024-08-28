<script lang="ts">
  import { theme } from "../stores/settings.ts";
</script>

<header style="--primary_color: {$theme.primary_color}">
  <div class="left">sidebar-button</div>
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
