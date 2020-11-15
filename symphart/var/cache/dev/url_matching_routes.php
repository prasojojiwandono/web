<?php

/**
 * This file has been auto-generated
 * by the Symfony Routing Component.
 */

return [
    false, // $matchHost
    [ // $staticRoutes
        '/' => [
            [['_route' => 'article_list', '_controller' => 'App\\Controller\\ArticleController::index'], null, null, null, false, false, null],
            [['_route' => 'index', '_controller' => 'App\\Controller\\ArticleController::index'], null, null, null, false, false, null],
        ],
        '/article/new' => [[['_route' => 'new_article', '_controller' => 'App\\Controller\\ArticleController::new'], null, null, null, false, false, null]],
        '/article/save' => [[['_route' => 'app_article_save', '_controller' => 'App\\Controller\\ArticleController::save'], null, null, null, false, false, null]],
    ],
    [ // $regexpList
        0 => '{^(?'
                .'|/_error/(\\d+)(?:\\.([^/]++))?(*:35)'
                .'|/article/(?'
                    .'|edit/([^/]++)(*:67)'
                    .'|delete/([^/]++)(*:89)'
                    .'|([^/]++)(*:104)'
                .')'
            .')/?$}sDu',
    ],
    [ // $dynamicRoutes
        35 => [[['_route' => '_preview_error', '_controller' => 'error_controller::preview', '_format' => 'html'], ['code', '_format'], null, null, false, true, null]],
        67 => [[['_route' => 'edit_article', '_controller' => 'App\\Controller\\ArticleController::edit'], ['id'], null, null, false, true, null]],
        89 => [[['_route' => 'app_article_delete', '_controller' => 'App\\Controller\\ArticleController::delete'], ['id'], null, null, false, true, null]],
        104 => [
            [['_route' => 'article_show', '_controller' => 'App\\Controller\\ArticleController::show'], ['id'], null, null, false, true, null],
            [null, null, null, null, false, false, 0],
        ],
    ],
    null, // $checkCondition
];
