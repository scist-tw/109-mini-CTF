<ul>
<?php foreach($_SESSION['files'] as $value): ?>
    <li><a href="/upload/<?= $value ?>"><?= $value ?></a></li>
<?php endforeach; ?>
<ul>
