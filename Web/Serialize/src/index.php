<?php
if (isset($_GET['logout'])) {
    setcookie('user','');
    header("Location: /");
    exit;
}

ob_start();

include_once 'header.php';
include_once 'lib.php';
include_once 'user.php';
include_once 'footer.php';
