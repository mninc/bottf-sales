<html>
<head>
    <title>Bot.tf Sales</title>
    <link rel="stylesheet" type="text/css" href="bottfsales.css">
    <!--<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css" /><link rel="stylesheet" href="https://bot.tf/assets/css/bootstrap.min.css" /><link rel="stylesheet" href="https://bot.tf/assets/css/my.css?v=1518114354" />
-->
</head>
<body>
<div class="head">
<p align="center">Find some trades by entering an item into the box below. (You can also enter a bot.tf trade ID, if you know it)</p>
<form method='get' action='/bottf-sales.php'>
    <p>
    <?php
    if (isset($_GET["page"])) {
        echo "Go to item: <input type=\"text\" value=\"". htmlspecialchars($_GET["page"]) . "\" name=\"page\" > ";
        } else {
        echo "Go to item: <input type=\"text\" value=\"\" name=\"page\" > ";
    }
    ?>
        <input type="submit" ></p>

</form>
</div>
<div class="container" >
    <div class="col-md-10 col-md-offset-1" >
<?php
error_reporting(E_ALL);
ini_set("display_errors", true);

if (!isset($_GET["page"])) {
    echo "<p>Please enter an item!</p>";
} elseif (file_exists("/var/www/bottf-sales/" . str_replace("&amp;", "&", htmlspecialchars($_GET["page"], ENT_QUOTES)) . ".html")) {
    echo nl2br(file_get_contents("/var/www/bottf-sales/" . str_replace("&amp;", "&", htmlspecialchars($_GET["page"], ENT_QUOTES)) . ".html"));
    //include "/var/www/bottf-sales/" . $_GET["page"] . ".html";
} else {
    echo "<p>Not a valid page! Check punctuation, spelling and cases.</p>";
}
?>
</div>
</div>

<script src="https://bot.tf/assets/js/jquery.min.js"></script>

<script src="https://bot.tf/assets/js/bootstrap.min.js"></script>
<script src="https://bot.tf/assets/js/my.js?v=1518114354"></script>
    <a href="bottf-sales-about.php" style="display:inline-block;">about</a>
<br><br>

</body>
</html>
