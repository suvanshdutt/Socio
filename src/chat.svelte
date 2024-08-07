<script lang="ts">
    export let chat_name: string = '';
    export let chat_profile_picture: string = '';
    export let onSelect: () => void = () => {};
  
    function handleClick() {
      onSelect();
    }
  </script>
  
  <button class="chat-item" on:click={handleClick} aria-label={`Chat with ${chat_name}`}>
    <img src={chat_profile_picture} alt={chat_name} class="profile-picture"/>
    <p class="chat_name">{chat_name}</p>
  </button>
  
  <style>
    .chat-item {
      display: flex;
      align-items: center;
      padding: 10px;
      cursor: pointer;
      border: none;
      background: none;
      text-align: left;
      width: 100%;
    }
  
    .chat_name {
        color: aliceblue;
        font-size: large;
    }

    .profile-picture {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      margin-right: 10px;
    }
  
    .chat-item:hover {
      background-color: rgba(50,50,50,0.5);
    }
  </style>
  