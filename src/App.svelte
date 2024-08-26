<script lang="ts">
  import Chat from './chat.svelte';

  interface ChatMessage {
    content: string;
  }

  interface ChatData {
    name: string;
    profile_picture: string;
    messages: ChatMessage[];
  }

  interface FetchedChatData {
    _id: string;
    participants: string;
    messages: any[];
  }

  let chats: ChatData[] = [
    { name: 'Alice', profile_picture: '../public/blank.png', messages: [{ content: 'Hi!' }, { content: 'How are you?' }] },
    { name: 'Bob', profile_picture: '../public/blank.png', messages: [{ content: 'Hello!' }, { content: 'What’s up?' }] }
  ];

  let selectedChat: ChatData | null = null;

  function handleChatSelect(chat: ChatData) {
    selectedChat = chat;
    fetchMessages();
  }

  // Enter key triggers send button
  
  const handleKeyUp = (event: KeyboardEvent): void => {
    const sendButton = document.getElementById('send-button') as HTMLButtonElement | null;
    
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault(); // Prevent newline character
      if (sendButton) {
        sendButton.click(); // Trigger click on send button
      }
    }
  };

  // sends the message and clears the textarea

  function handleSendClick() {
    const textarea = document.getElementById('message-input') as HTMLTextAreaElement | null;
    if (textarea && textarea.value.trim() !== '') {
      sendMessage(textarea.value.trim());
      textarea.value = ''; // Clear the input field
    }
  }

  // sending messages
  async function sendMessage(content: string) {
  if (selectedChat) {
    try {
      const response = await fetch('http://localhost:8000/chat/chats/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          participants: selectedChat.name,
          messages: [{ content }],
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to send message');
      }

      const data = await response.json();
      console.log('Message sent:', data);

      // Update the UI with the new message
      selectedChat.messages.push({ content });
    } catch (error) {
      console.error('Error sending message:', error);
    }
  }
}

  // fetching messages

  async function fetchMessages() {
  try {
    const response = await fetch('http://localhost:8000/chat/chats/');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    console.log('Fetched messages:', data);
    console.log(data.chats[0].messages);
    
    // Ensure data.chats is an array
    if (Array.isArray(data.chats)) {
      // Update chats with the fetched messages
      data.chats.forEach((fetchedChat: FetchedChatData) => {
        const existingChatIndex = chats.findIndex(chat => chat.name === fetchedChat.participants);
        if (existingChatIndex !== -1) {
          // Update the existing chat with the fetched messages
          chats[existingChatIndex].messages = [...chats[existingChatIndex].messages, ...fetchedChat.messages];
        }
      });
    } else {
      console.error('Expected an array of chats');
    }
  } catch (error) {
    console.error('Error fetching messages:', error);
  }
}


</script>

<main>
  <div class="title">
    <h1>
      Socio
    </h1>
  </div>

  <div class="row">
    <div class="column-left">
      {#each chats as chat}
        <Chat
          chat_name={chat.name}
          chat_profile_picture={chat.profile_picture}
          onSelect={() => handleChatSelect(chat)}
        />
      {/each}
    </div>

    <div class="column-right">
      {#if selectedChat}
        <div class="chat-box">
          <div class="profile">
            <img src={selectedChat.profile_picture} alt="{selectedChat.name}'s profile picture" class="profile-picture"/>
            <p class="chat_name">{selectedChat.name}</p>
          </div>
          <div class="messages">
            {#each selectedChat.messages as { content }}
              <p class="msg">{content}</p>
            {/each}
          </div>
          <textarea id="message-input" placeholder="Type a message..." on:keypress={handleKeyUp}></textarea>
          <button id="send-button" aria-label="Send Message" on:click={handleSendClick} >
            <!-- SVG arrow pointing top-right -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path 
              d="M21.707 2.293a1 1 0 0 0-1.069-.225l-18 7a1 1 0 0 0 .145 1.909l8.379 1.861 1.862 8.379a1 1 0 0 0 .9.78L14 22a1 1 0 0 0 .932-.638l7-18a1 1 0 0 0-.225-1.069zm-7.445 15.275L13.1 12.319l2.112-2.112a1 1 0 0 0-1.414-1.414L11.681 10.9 6.432 9.738l12.812-4.982z" 
              style="fill:#1c1b1e" data-name="Share"/>
            </svg>
          </button>
        </div>
      {:else}
        <p>Select a chat to view messages.</p>
      {/if}
    </div>

  </div>
</main>






<style>
  .title {
    height: 72px;
    text-align: center;
    line-height: 72px;
  }

  .title h1 {
    font-size: 3rem;
    color: transparent; 
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); 
    margin: 0; 
    padding: 0.5rem;
    font-family: 'Roboto', sans-serif; 
    text-transform: uppercase;
    letter-spacing: 1px;
    background: linear-gradient(135deg, #6a0dad, #a87fce);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
  }

  .column-left{
    width: 35%;
    background-color: #131517;
    color: #cfcfd2;
    overflow-y: auto;
  }

  .column-right{
    width: 65%;
    background-color: #0f1012;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    position: relative;
  }

  .row {
    display: flex;
    height: 90vh;
  }

  .profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .chat_name {
    margin-left: 10px;
    color: aliceblue;
    font-size: x-large;
  }

  .chat-box {
    display: flex;
    flex-direction: column;
    flex: 1;
    padding: 10px;
    box-sizing: border-box;
    position: relative;
  }

  .profile {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .messages {
    flex:1;
    overflow-y: auto;
  }

  .msg {
    font-size: medium;
  }

  #send-button {
    position: absolute;
    bottom: 16px;
    right: 16px;
    width: 40px;
    height: 40px;
    background-color: rgba(211,211,211,1);
    border: none;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
  }

  #send-button svg {
    width: 25px;
    height: 25px;
    fill: aliceblue;
  }

  #send-button:hover {
    background-color: rgba(241,241,241,1);
    transform: scale(1.1);
  }
</style>