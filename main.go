package main 

import (
    "fmt"
    "net/http"
    "golang.org/x/oauth2/clientcredentials"
    "golang.org/x/oauth2/twitch"
)

func main() {
    var token string 
    token = ""
    client := &http.Client{}
    req, err := http.NewRequest("GET", "https://api.twitch.tv/helix/users", nil)
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }
    req.Header.Set("Authorization", "Bearer "+accessToken)
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error making request:", err)
        return
    }
    defer resp.Body.Close()
    fmt.Println(resp.StatusCode)
}
