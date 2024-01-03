#!/usr/bin/node

const fs = require( 'fs' );
const file = process.argv[ 2 ];

fs.readFile( file, 'utf8', ( err, data ) =>
{
    if ( err )
    {
        return console.error( err );
    } else
    {
        console.log( data );
    }
} );
