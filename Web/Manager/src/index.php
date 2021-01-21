<?php
session_start();
if(!isset($_SESSION['files']))
    $_SESSION['files'] = [];
$action = $_GET['action'] ?? 'welcome.php';
$list = Array(
    'Welcome' => '/?action=welcome.php',
    'Upload' => '/?action=upload.php',
    'Files' => '/?action=files.php',
    'Hint' => '/show.php',
);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <style>
        html, body {
            height: 100%;
        }
        .container {
            min-height: calc(100% - 4rem);
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-center">
        <a class="navbar-brand" href="/">Manager</a>
        <ul class="navbar-nav">
            <?php foreach($list as $key => $value): ?>
                <li class="nav-item">
                    <a class="nav-link" href="<?= $value ?>"><?= $key ?></a>
                </li>
            <?php endforeach; ?>
        </ul>
    </nav>
    <div class="container d-flex align-items-center justify-content-center flex-column">
        <?php include_once 'module/' . $action ?>
    </div>
</body>
</html>
