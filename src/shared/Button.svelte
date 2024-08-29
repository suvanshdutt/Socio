<script lang="ts">
  import { theme } from "../stores/settings.ts";
  export let type: string = "primary";
  export let flat: boolean = false;
  export let inverse: boolean = false;
</script>

<button
  class={type}
  class:flat
  class:inverse
  style="--primary_color={$theme.primary_color};
    --secondary_color: {$theme.secondary_color};
    --text_color: {$theme.text_color}"
  on:click
>
  <slot></slot>
</button>

<style>
  button {
    border: 0;
    cursor: pointer;
    border-radius: 10px;
    padding: 6px 12px;
    box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.3);
  }
  .primary {
    background: var(--primary_color);
    color: var(--text_color);
  }
  .secondary {
    background: var(--secondary_color);
    color: var(--text_color);
  }
  .flat {
    box-shadow: none;
  }
  .primary.inverse {
    background: var(--text_color);
    color: var(--primary_color);
  }
  .secondary.inverse {
    background: var(--text_color);
    color: var(--secondary_color);
  }
</style>
