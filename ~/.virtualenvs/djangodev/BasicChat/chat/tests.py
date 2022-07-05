"""
Automated tests for the chat server. Makes sure the server runs as intended
and doesn't break.
"""

from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True

    @classmethod
    def setUpClass(cls):
        """Tests the setting up of the class"""
        super().setUpClass()
        try:
            cls.driver = webdriver.Chrome()
        except:
            super.tearDownClass()
            raise
    
    @classmethod
    def tearDownClass(cls):
        """Deconstructs the class"""
        cls.driver.quit()
        super().tearDownClass()

    def seen(self):
        """Tests that when a chat message is posted, it is seen
        by everybody in the same room.
        """
        try:
            self._enter_room('gdbg')

            self._open_new_window()
            self._enter_room('DEI')

            self._switch_to_window(0)
            self._post_message('Hello there')
            WebDriverWait(self.driver, 2).until(lambda _:
                'Hello there' in self._chat_log_value,
                "Message from window 1 was not received by window 1")
            
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(lambda _:
                'Hello there' in self._chat_log_value,
                "Message from window 1 was not received by window 2")
        finally:
            self._close_all_new_windows()
    
    def not_seen(self):
        """Tests that when a chat message is posted, it is not
        seen by people in another room
        """
        try:
            self._enter_room('gdbg')

            self._open_new_window()
            self._enter_room('DEI')

            self._switch_to_window(0)
            self._post_message('Hello there')
            WebDriverWait(self.driver, 2).until(lambda _:
                'Hello there' in self._chat_log_value,
                "Message from window 1 was not received by window 1")
            
            self._switch_to_window(1)
            self._post_message('General Kenobi')
            WebDriverWait(self.driver, 2).until(lambda _:
                'General Kenobi' in self._chat_log_value,
                "Message from window 2 was not received by window 2")
            self.assertTrue('Hello there' not in self._chat_log_value,
                "Message from window 1 was improperly received by window 2")
        finally:
            self._close_all_new_windows()

        # *** Utility functions ***

        def _enter_room(self, room_name):
            """Enters the specified chat room.
            Argument:
              `room_name`: the name of the room to enter
            """
            self.driver.get(self.live_server_url + '/chat/')
            ActionChains(self.driver).send_keys(room_name + '\n').perform()
            WebDriverWait(self.driver, 2).until(lambda _:
                room_name in self.driver.current_url)
            
        def _open_new_window(self):
            """Opens a new window and switches the current window to it"""
            self.driver.execute_script('window.open("about:bank", "_blank");')
            self._switch_to_window(-1)
        
        def _close_all_new_windows(self):
            """Closes all windows except the initial one."""
            while len(self.driver.window_handles) > 1:
                self._switch_to_window(-1)
                self.driver.execute_script('window.close();')
            if len(self.driver.window_handles) == 1:
                self._switch_to_window(0)

        def _switch_to_window(self, win_idx):
            """Switches to the selected window.
            Argument:
              `win_idx`: The window to switch to (0 indexed)
            """
            self.driver.switch_to.window(self.driver.window_handles[win_idx])

        def _post_message(self, message):
            """Sends a message.
            Argument:
              `message`: The message to send
            """
            ActionChains(self.driver).send_keys(message + '\n').perform()

        @property
        def _chat_log_value(self):
            """Gets the last message from the chat log"""
            return self.driver.find_element(by=By.CSS_SELECTOR, value="#chat-log").get_property('value')