import { writable, type Writable } from "svelte/store";

type Theme = {
    text_color: string;
    background_color: string;
    primary_color: string;
    secondary_color: string;
    accent_color: string;
};

export const _theme: Theme = {
    text_color: "#050315",
    background_color: "#e6e6e6",
    primary_color: "#7451ff",
    secondary_color: "#9f97e0",
    accent_color: "#5544d6",
};

export const theme: Writable<Theme> = writable(_theme);
