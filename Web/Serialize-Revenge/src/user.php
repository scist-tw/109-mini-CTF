<?php
include_once 'lib.php';

$user = NULL;
if (isset($_COOKIE['user']))
    $user = unserialize(base64_decode($_COOKIE['user']));
if (isset($_POST['username']))
    $user = new User($_POST['username']);

if (!$user) {
    include 'login.php';
    return;
}
setcookie('user', base64_encode(serialize($user)));
?>

<div class="row align-items-center">
    <span class="col-auto">Welcome, <?= $user ?></span>
    <a href="/?logout" class="col-auto">
        <button type="submit" class="btn btn-primary">Logout</button>
    </a>
</div>
